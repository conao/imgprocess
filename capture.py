import cv2

def capture(mirror = True):
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        if mirror is True:
            frame = frame[:,::-1]
            
        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:    # exit push escape key(27)
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

capture()
