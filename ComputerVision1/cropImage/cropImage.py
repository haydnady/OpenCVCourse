# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2

source = cv2.imread("sample.jpg", 1)

# Make a dummy image, will be useful to clear the drawing.
dummy = source.copy()

cv2.namedWindow("Window")



# Lists to store the points
center=[]
circumference=[]


def cropImage(action, x, y, flags, userdata):
  # Referencing global variables
  global center, circumference
  # Action to be taken when left mouse button is pressed
  if action == cv2.EVENT_LBUTTONDOWN:
    center = [(x, y)]
    # Mark the center
    cv2.circle(source, center[0], 1, (255, 255, 0), 2, cv2.LINE_AA)

  # Action to be taken when left mouse button is released
  elif action == cv2.EVENT_LBUTTONUP:
    circumference = [(x, y)]
    # Calculate radius of the circle
    radius = math.sqrt(math.pow(
        center[0][0]-circumference[0][0], 2)+math.pow(center[0][1]-circumference[0][1], 2))
    # Draw the circle
    cv2.circle(source, center[0], int(radius), (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Window", source)



# highgui function called when mouse events occur
cv2.setMouseCallback("Window", cropImage)

k = 0
# Loop until escape character is pressed
while k!=27 :
    cv2.imshow("Window", source)
    cv2.putText(source, "Choose top left corner, and drag,?", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    k = cv2.waitKey(20) & 0xFF
    # Another way of cloning
    if k==99:
        source= dummy.copy()

cv2.destroyAllWindows()


