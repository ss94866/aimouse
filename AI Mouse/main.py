import numpy as np
import cv2 
import mediapipe as mp
import utils
import time
import pyautogui as pa


stime = 0
etime = 0
smoothen = 2
k = 25
plox, ploy = 0,0
clox, cloy = 0,0
old_dist = 0

scr_width, scr_height = pa.size()
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    height, width, _ = frame.shape
    mouse = utils.AIMOUSE(frame)
    frame = mouse.pre_process()
    x, y, xm, ym= mouse.tip_reult(frame)
    dist = mouse.dist(x, y, xm, ym)
    
    
    if x != None and y != None:
        if xm != None and ym != None:
            cv2.circle(frame,(x,y), 10, (255,0,255), 5)
            cv2.circle(frame,(xm,ym), 10, (255,255,0), 5)

    fps, stime = utils.AIMOUSE.calc_fps(stime, etime)
    x1,y1,x2,y2= mouse.get_box()
    if x and y is not None:
        w,h = mouse.get_point(x, y, x1, y1, x2, y2)
        if h >= 0 and h <= 1:
            if w >= 0 and w <= 1:
                if dist >= (old_dist - k):
                    # print(f'dist {dist} , old_value {old_dist - k}')
                    pointx = plox + ((int(w * scr_width) - plox) / smoothen)
                    pointy = ploy + ((int(h * scr_height) - ploy) / smoothen) 
                    # print(int(w * scr_width),int(h * scr_height))
                    pa.moveTo(int(pointx),int(pointy))
                    plox, ploy = pointx, pointy
                    old_dist = dist
    # print(dist)               
    if dist is not None:
        if dist < 34:
            pa.click()

    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    cv2.putText(frame,"FPS:" + str(int(fps)), (50,height-50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255),2,cv2.LINE_AA)
    cv2.imshow('frame', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()