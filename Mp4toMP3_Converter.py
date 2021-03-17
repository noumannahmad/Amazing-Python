# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 01:01:53 2021

@author: Nouman Ahmad
"""

import imageio
import moviepy.editor

video=moviepy.editor.VideoFileClip("File.mp4")


audio=video.audio
audio.write_audiofile("output.mp3")
print("Converted Sucessfully")