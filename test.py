import cv2

cap = cv2.VideoCapture(0)

while (1):
    _, image = cap.read()
    cv2.imshow("show", image)
    can = cv2.Canny(image, 25, 255, None, None, 1)
    cv2.imshow("can", can)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()