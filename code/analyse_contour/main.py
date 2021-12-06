#!/usr/bin/python
import numpy as np
import cv2

image = cv2.imread('perfect_circle.jpg')
output = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,100)
if circles is not None:
    print("trouve")
	# convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
    cv2.imshow(output, np.hstack([image, output]))
    cv2.waitKey(0)
#window_name = 'image'
#cv2.imshow(window_name,image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()