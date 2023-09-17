from flask import Flask, render_template, Response
import facial2

#Initialize the Flask app
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index() -> str:
    return render_template('index.html')

# streaming
@app.route('/video_feed.html')
def video_feed() -> Response:
    """
    Render the video feed from facial.
    """
    return Response(facial2.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# video_player page
@app.route('/video_player.html')
def video_player():
    """
    Render video_player.
    """
    return render_template('video_player.html')

# about page
@app.route('/about.html')
def about():
    """
    Render the about page.
    """
    return render_template('about.html')


import chat
# analysis page
@app.route('/analysis.html')
def analysis():
    """
    Render the analysis page.
    """
    chat.reset()
    chat.analysis()
    image_url = 'static/images/emotion_pie_chart.png'
    return render_template('analysis.html', summary=chat.final_summary, 
                            prediction = chat.final_predictions,
                            image_url = image_url)

@app.route('/quit')
def quit_facial() -> str:
    """
    Quit the facial scanner.
    """
    global quit_flag  # have to make global so it changes outside of function
    quit_flag = True
    return "Video terminated."

if __name__ == "__main__":
    app.run()