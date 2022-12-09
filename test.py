import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('window',frame)
    else:
        print('khong co data')

    cv2.waitKey(0)