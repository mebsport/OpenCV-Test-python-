
import numpy as np
import cv2
import cv2

# Load an image and save to a variable named img
img = cv2.imread('Images/FROM_ROBOT_1-2-24/REDRIGHT.jpg')

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
mask = cv2.inRange(hsv, lowerBlue, highBlue)
bwMask = cv2.inRange(grayImg, lowTile, highTile)

# Save the images to a file
cv2.imwrite('output.jpg', mask)
cv2.imwrite('bwMask.jpg', bwMask)
cv2.imwrite('hsv.jpg', hsv)
cv2.imwrite('bw.jpg', grayImg)

# Convert blue to HSV
# hsv_blue = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)


def crop_image(image, x, y, width, height):
    cropped_image = image[y:y+height, x:x+width]
    return cropped_image

# img = cv2.imread('Images/FROM_ROBOT_1-2-24/REDRIGHT.jpg')
img = mask

# Left
cropped_img = crop_image(img, 0, 427, 357, 293)
cv2.imwrite('left_cropped_image.jpg', cropped_img)
leftCount = np.count_nonzero(cropped_img)

#Right
cropped_img = crop_image(img, 898, 427, 357, 293)
cv2.imwrite('right_cropped_image.jpg', cropped_img)
rightCount = np.count_nonzero(cropped_img)


#Center
cropped_img = crop_image(img, 386, 427, 462, 165)
cv2.imwrite('center_cropped_image.jpg', cropped_img)
midCount = np.count_nonzero(cropped_img)

highNum = max(leftCount,rightCount,midCount)

if(highNum == leftCount):
    print("Left")
elif(highNum == rightCount):
    print("Right")
else:
    print("Center")



