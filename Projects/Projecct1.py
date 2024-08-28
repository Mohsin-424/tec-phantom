
# OpenCV Basics 
import cv2

# image = cv2.imread("Projects/3.jpg")
image = cv2.imread("Projects/1.png")


# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.bitwise_not(image)

assert image is not None, "Failed to load image"
cv2.imshow("   This is processes image" , image)
cv2.waitKey(0)

cv2.destroyAllWindows()