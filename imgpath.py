import cv2
img = cv2.imread("images.jpg",0)
cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
#cv2.destroyAllWindows()
