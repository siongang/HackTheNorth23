import cv2
import numpy as np

# get video
cam = cv2.VideoCapture(0)

# load pretrained model
model = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = model.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in model.getUnconnectedOutLayers()]

# output details
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(layer_names), 3))

while 1:
    # get frame as np.array
    _, frame = cam.read()

    # prep model for object detection
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    model.setInput(blob)
    outs = model.forward(output_layers)  # forward propagate for outputs

    # 
    height, width, channels = frame.shape
    class_ids = []
    confidences = []
    boxes = []

    # draw detection boundaries, do we need?
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Adjust confidence threshold as needed
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # display frame
    cv2.imshow('frame_name', frame)

    # exit key
    if cv2.waitKey(1) == ord('q'):
        break

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes and labels
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(layer_names[class_ids[i]])
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)

# terminate
cam.release()
cv2.destroyAllWindows()