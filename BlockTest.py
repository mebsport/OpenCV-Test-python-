
import numpy as np
import cv2
import random
import numpy as np
import cv2
import random

#Load an image
img = cv2.imread('Images/BLUE_CENTER.jpg')

if img is None:
    print('Failed to load image file:')
    sys.exit(1)

#Variables
blue = np.uint8([[[36,52,93]]])
red = np.uint8([[[125,29,14]]])

lowerBlue = np.array([[[  0, 50,  50]]])
highBlue = np.array([[[  28, 255,  255]]])
lowerRed = np.array([[[94, 50, 50]]])
highRed = np.array([[[136, 255, 2555]]])

# Convert image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lowerBlue, highBlue)

# Save the image to a file
cv2.imwrite('output.jpg', mask)

# Convert blue to HSV
# hsv_blue = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)


