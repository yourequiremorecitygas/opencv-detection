# OpenCV 라이브러리 임포트
import cv2
import numpy as np
 
# 이미자 압력
image = cv2.imread("img.png")

# 원본 이미지를 회색조로 변환
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

light_orange = (180, 0, 0)
dark_orange = (270, 255, 255)

mask = cv2.inRange(hsv_image, light_orange, dark_orange)

Bmask = cv2.inRange(hsv_image, np.array([100, 80, 80]), np.array([140, 255, 255]))
Gmask = cv2.inRange(hsv_image, np.array([35, 80, 80]), np.array([80, 255, 255]))


mask1 = cv2.inRange(hsv_image, np.array([0, 70, 50]), np.array([10,255,255]))

Rmask = cv2.inRange(hsv_image, np.array([170, 70, 50]), np.array([180, 255, 255]))

mask = mask1 | Rmask

result = cv2.bitwise_and(image, image , mask=mask)
# 원본 이미지와 회색조 이미지를 각각 Widnows로 출력
#cv2.imshow("Landscape", image)
#cv2.imshow("Landscape - gray", gray_image)

cv2.imshow("Original",image)
cv2.imshow("RedDetection",result)
#cv2.imshow("d2",gray_image)

# ESC 키 입력 시 Windows 닫음
cv2.waitKey(0)
cv2.destroyAllWindows()