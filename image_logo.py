import cv2
import numpy as np


logo = cv2.imread("put your logo path here..")
h_logo, w_logo, _ = logo.shape

img = cv2.imread("put path of which image you want to watermark.")
h_img, w_img, _ = img.shape

center_y = int(h_img / 2)
center_x = int(w_img / 2)
top_y = center_y - int(h_logo / 2)
left_x = center_x - int(w_logo / 2)
bottom_y = top_y + h_logo
right_x = left_x + w_logo

# cv2.circle(img, (left_x, top_y), 10, (0, 255, 0), -1)
# cv2.circle(img, (right_x, bottom_y), 10, (0, 255, 0), -1)

# Get ROI
roi = img[top_y: bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 1, logo, 0.3, 0)

img[top_y: bottom_y, left_x: right_x] = result

# cv2.imshow('roi', roi)
# cv2.imshow('result', result)
cv2.imshow("img", img)
# cv2.imshow("logo", logo)
cv2.waitKey(0)
