# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:35:25 2021

@author: Nouman Ahmad
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 02:00:15 2021

@author: Nouman Ahmad
"""

#http://blog.alivate.com.au/poppler-windows/


from tkinter import filedialog as fd
filename = fd.askopenfilename()

from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
 
print(filename)
 
def pdf2img():
    try:
        images = convert_from_path(filename,dpi=200,poppler_path=r'poppler-0.68.0\bin')
        for i, image in enumerate(images):
            fname = 'image'+str(i)+'.png'
            image.save(fname, "PNG")

    except  :
        Result = "NO pdf found"
        messagebox.showinfo("Result", Result)
 
    else:
        Result = "success"
        messagebox.showinfo("Result", Result)
 
master = Tk()
Label(master, text="File Location").grid(row=0, sticky=W)
 
b = Button(master, text="Convert", command=pdf2img)
b.grid(row=0, column=2,columnspan=2, rowspan=2,padx=5, pady=5)
  
mainloop()