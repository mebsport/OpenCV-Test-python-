# import colorsys
import cv2
import numpy as np

# rgb_color = (160, 68, 64)
# hsv_color = colorsys.rgb_to_hsv(rgb_color[0]/255 * 180, rgb_color[1]/255, rgb_color[2]/255)

# print(hsv_color)

red = np.uint8([[[160,68,64]]])
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
print(hsv_red)
