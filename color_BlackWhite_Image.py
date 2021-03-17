# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:22:33 2021

@author: Nouman Ahmad
"""

import cv2


img =cv2.imread("image.PNG",0)

rs=cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
print(type(img))
cv2.imwrite("black.png",rs)

cv2.imshow('show',img)
cv2.waitKey(400)

cv2.destroyAllWindows()