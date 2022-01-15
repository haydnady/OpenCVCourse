# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import cv2


def cropImage(action, x, y, flags, userdata):
  # Referencing global variables 
  global center, circumference
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    center=[(x,y)]
    # Mark the center
    cv2.circle(source, center[0], 1, (255,255,0), 2, cv2.LINE_AA );

  # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    circumference=[(x,y)]
    # Calculate radius of the circle
    radius = math.sqrt(math.pow(center[0][0]-circumference[0][0],2)+math.pow(center[0][1]-circumference[0][1],2))
    # Draw the circle
    cv2.circle(source, center[0], int(radius), (0,255,0),2, cv2.LINE_AA)
    cv2.imshow("Window",source
    

source = cv2.imread("sample.jpg", 1)

# Make a dummy image, will be useful to clear the drawing.
dummy = source.copy()

cv2.namedWindow("Window")

# highgui function called when mouse events occur
cv2.setMouseCallback("Window", cropImage)

# Loop until escape character is pressed
while True:
    cv2.imshow("Window", source)
    cv2.putText(source, "Choose top left corner, and drag,?", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

cv2.destroyAllWindows()


