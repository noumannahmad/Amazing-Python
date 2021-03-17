# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:46:17 2021

@author: Nouman Ahmad
"""
import cv2

vs=cv2.VideoCapture('Fall.mp4')


prop =cv2.CAP_PROP_FRAME_COUNT
total =int(vs.get(prop))
print("[INFO] {} total frame in video".format(total))

ret, img =vs.read()
print(ret)

count= 0

while ret:
    cv2.imwrite("Images//frame%d.jpg" %count,img)
    ret, img=vs.read()
    print('Read a new Frame:',ret)
    count += 1
    