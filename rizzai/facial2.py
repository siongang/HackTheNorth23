#Import necessary libraries
from flask import Flask, render_template, Response
from deepface import DeepFace
import cv2
#Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained emotion detection model
model = DeepFace.build_model("Emotion")

# Define emotion labels
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize cam object
camera = cv2.VideoCapture(0)

emotion_list = {}
quit_flag = False

def gen_frames() -> None:
    """
    Run the camera. Make predictions using the DeepFace model.
    """ 
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success or quit_flag:
            break

        # greyscale for efficiency
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract the face ROI (Region of Interest)
            face_roi = gray_frame[y:y + h, x:x + w]

            # Resize the face ROI to match the input shape of the model
            resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)

            # Normalize the resized face image
            normalized_face = resized_face / 255.0

            # Reshape the image to match the input shape of the model
            reshaped_face = normalized_face.reshape(1, 48, 48, 1)

            # Predict emotions using the pre-trained model
            preds = model.predict(reshaped_face)[0]
            emotion_idx = preds.argmax()
            emotion = emotion_labels[emotion_idx]
            
            if not emotion in emotion_list:
                emotion_list[emotion] = 1
            else:
                emotion_list[emotion] += 1
        
            # Draw rectangle around face and label with predicted emotion
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)


        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index() -> str:
    return render_template('index.html')

# streaming
@app.route('/video_feed')
def video_feed() -> Response:
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# video_player page
@app.route('/video_player.html')
def video_player():
    return render_template('video_player.html')

@app.route('/')
def quit_facial() -> str:
    global quit_flag  # have to make global so it changes outside of function
    quit_flag = True
    return "Video terminated."

def get_emotion_list() -> dict:
    """
    Returns current emotion_list 
    """
    return emotion_list

if __name__ == "__main__":
    app.run(debug=True)
    print(get_emotion_list())