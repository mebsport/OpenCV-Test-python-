
import numpy as np
import cv2

# Load an image and save to a variable named img
img = cv2.imread('Images/RED_CENTER.jpg')

# check to make sure the immage exists so no errors occur
if img is None:
    print('Failed to load image file:')
    sys.exit(1)

# create a grayscale copy of the image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Variables
blue_BAD = np.uint8([[[36,52,93]]])
red_BAD = np.uint8([[[125,29,14]]])


lowerBlue = np.array([[[  105, 50,  50]]])
highBlue = np.array([[[  125, 255, 255]]])

lowerRed = np.array([[[-5, 50, 50]]])
highRed = np.array([[[15, 255, 255]]])

lowTile = np.array([[[  110,  110,  110]]])
highTile = np.array([[[  160, 160, 160]]])

lowWhite = np.array([[[  235,  235,  235]]])
highWhite = np.array([[[  255, 255, 255]]])

# Convert image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# use a mask on the HSV image to get only wanted colors
mask = cv2.inRange(hsv, lowWhite, highWhite)
bwMask = cv2.inRange(grayImg, lowTile, highTile)

# Save the images to a file
cv2.imwrite('output.jpg', mask)
cv2.imwrite('bwMask.jpg', bwMask)
cv2.imwrite('hsv.jpg', hsv)
cv2.imwrite('bw.jpg', grayImg)

# Convert blue to HSV
# hsv_blue = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)


