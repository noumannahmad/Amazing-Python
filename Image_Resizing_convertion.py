# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:43:33 2021

@author: Nouman Ahmad
"""

from PIL import Image

image =Image.open("image.png")
#rgb_img=image.convert("RGB")
#rgb_img.save("convertedimg.jpg")

width,height =image.size
print(width,'x',height)

#224 x 224

img=image.resize((224,224))

rgb_img=img.convert("RGB")
rgb_img.save("resizeimage.jpg")