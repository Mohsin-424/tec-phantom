#pylint:disable=no-member

import cv2 as cv

img = cv.imread('f:/Techphantom/Libraries/opencv-course-master/Resources/Photos/cat.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('f:/Techphantom/Libraries/opencv-course-master/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('q'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
