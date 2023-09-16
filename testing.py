import cv2

#print('h')

import cv2

cam = cv2.VideoCapture(0)

while 1:
    # get frame as np.array
    _, frame = cam.read()

    # display frame
    cv2.imshow('frame_name', frame)

    # exit key
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()