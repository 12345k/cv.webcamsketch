import cv2
import numpy as np

#sketch function
def webcamsketch(image):
	img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
	canny_edges = cv2.Canny(img_gray_blur, 10, 70)
	ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
	return mask

# start web cam
cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', webcamsketch(frame))
    #Press ESQ key
    if cv2.waitKey(1) == 13:
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
