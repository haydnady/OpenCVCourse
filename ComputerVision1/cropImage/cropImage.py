# Import libraries
import cv2


source = cv2.imread("sample.jpg", 1)

# Make a dummy image, will be useful to clear the drawing.
dummy = source.copy()

cv2.namedWindow("Window")

# Lists to store the points
pt1 = []
pt2 = []

# Exit variable, program wil exit when equals 1
stopProgram = 0

def cropImage(action, x, y, flags, userdata):
    global pt1, pt2, stopProgram

    # Action to be taken when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        pt1 = [(x, y)]

        # Mark top left corner
        cv2.rectangle(source, pt1[0], pt1[0], (255, 255, 0), thickness=2, lineType=cv2.LINE_8)


    # Action to be taken when left mouse button is released
    elif action == cv2.EVENT_LBUTTONUP:
        pt2 = [(x, y)]

        # Bottom right corner
        cv2.rectangle(source, pt1[0], pt2[0], (255, 255, 0), thickness=2, lineType=cv2.LINE_8)
        cv2.imshow("Window", source)

        # [rows, columns]
        croppedImage = source[pt1[0][1]:pt2[0][1], pt1[0][0]:pt2[0][0]]
        cv2.imwrite("face.png", croppedImage)
        # stopProgram = 1

def main():
    global source
    k = 0
    
    # highgui function called when mouse events occur
    cv2.setMouseCallback("Window", cropImage)

    # Loop until escape character is pressed or user created crop bounding box
    while k!=27 and not stopProgram:
        cv2.imshow("Window", source)

        cv2.putText(source, "Choose top left corner, and drag,?", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        k = cv2.waitKey(20) & 0xFF

        # Another way of cloning, when c is pressed on keyboard (clears back to original image).
        if k == 99:
            source = dummy.copy()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
