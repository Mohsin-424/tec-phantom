import cv2 as cv 
# img = cv.imread("f:/Techphantom/Libraries/opencv-course-master/Resources/Photos/cat.jpg")

# cv.imshow("Cat" , img)
# cv.waitKey(0)


# ..........To Read Video...............

# capture = cv.VideoCapture("f:/Techphantom/Libraries/opencv-course-master/Resources/Videos/dog.mp4")


# while True:
#     isTrue , frame = capture.read()
#     cv.imshow( "Dog Video" , frame )
#     if cv.waitKey(0) & 0xFF == ord("q"):
#         break
#     else:
#         break

# capture.release()
# cv.destroyAllWindows()




# ''''''''''''''''''''''''''''''."""""..."
# ..............Resize and Rescaling
# '''................"".....................






#pylint:disable=no-member
img = cv.imread('f:/Techphantom/Libraries/opencv-course-master/Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)
    
# Reading Videos

capture = cv.VideoCapture('f:/Techphantom/Libraries/opencv-course-master/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()











# ...........,,,,,,,................... Draw Shape and Put-Text ........................


