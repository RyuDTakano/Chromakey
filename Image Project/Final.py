
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
image = cv2.imread("C:/Users/notebook/Pictures/oo.jpg")
image = cv2.resize(image, (640, 480))
panel = np.zeros([1, 900], np.uint8)
#panel = np.zeros((100,700), np.uint8)
cv2.namedWindow('panel')

def nothing(x):
    pass

cv2.createTrackbar('LowerHue', 'panel', 0, 179, nothing)
cv2.createTrackbar('UpperHue', 'panel', 179, 179, nothing)

cv2.createTrackbar('LowerSat', 'panel', 0, 255, nothing)
cv2.createTrackbar('UpperSat', 'panel', 255, 255, nothing)

cv2.createTrackbar('LowerValue', 'panel', 0, 255, nothing)
cv2.createTrackbar('UpperValue', 'panel', 255, 255, nothing)

while True:
    _, Momentframe= cap.read()
    
    Momentframe = cv2.resize(Momentframe, (640, 480))
    #Momentframe = Momentframe[0: 480,0:640]

    hsv = cv2.cvtColor(Momentframe, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos('LowerHue', 'panel')
    u_h = cv2.getTrackbarPos('UpperHue', 'panel')
    l_s = cv2.getTrackbarPos('LowerSat', 'panel')
    u_s = cv2.getTrackbarPos('UpperSat', 'panel')
    l_v = cv2.getTrackbarPos('LowerValue', 'panel')
    u_v = cv2.getTrackbarPos('UpperValue', 'panel')
    
    lower_green = np.array([l_h, l_s, l_v])
    upper_green = np.array([u_h, u_s, u_v])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
    
    Masks = cv2.bitwise_and(Momentframe, Momentframe, mask=mask)
    gs = cv2.bitwise_and(Momentframe, Momentframe, mask=mask_inv)
    gun =  Momentframe - gs
    gun = np.where(gun == 0, image, gun)
    gs=gun
    cv2.imshow('Mask', Masks)
    cv2.imshow('Green_Sreen', gs)
    
    cv2.imshow('panel', panel)
    pressedKey = cv2.waitKey(1) & 0xFF
    k = cv2.waitKey(3) 
    if k == 2:  
       break
    elif pressedKey == ord('w'):
       print('w is pressed')
       break
cap.release()# if k == 2:
cv2.destroyAllWindows()