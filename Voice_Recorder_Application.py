# -*- coding: utf-8 -*-
"""


@author: Nouman Ahmad
"""

from tkinter import *
import sounddevice as sd
import soundfile as sf


def Voice_rec():
    fs=48000
    
    duration = 5
    myrecording =sd.rec(int(duration * fs),samplerate=fs,channels=2)
    sd.wait()
    
    return sf.write('audio_file.flac', myrecording, fs)

root =Tk()

Label(root,text="Voice Recording:").grid(row=0,sticky=W,rowspan=5)

btn =Button(root,text="start",command=Voice_rec())
btn.grid(row=0,column=2,columnspan=2,rowspan=2,padx=5,pady=5)

mainloop()    