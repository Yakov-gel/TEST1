import cv2

cap = cv2.VideoCapture(0)

while (1):
    _, image = cap.read()
    cv2.imshow("show", image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()