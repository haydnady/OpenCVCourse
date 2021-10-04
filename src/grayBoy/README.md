If you run into an error similar to this:
cv2.error: OpenCV(4.5.3) ....loadsave.cpp:803: error: (-215:Assertion failed) !_img.empty() in function 'cv::imwrite'


Check the image address again. This usually happens when the image is not loaded correctly in any way. Try giving the address directly; something like "C:\\test.jpg"