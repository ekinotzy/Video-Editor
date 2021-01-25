# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("dsa_geek.webm")

# Clipping of the video
# Getting video for only startig
# 10 seconds
clip = clip.subclip(0, 10)

# Rotating video by 180 degree
clip = clip.rotate(180)

# Reduce the audio volume ( volume x 0.5 )
clip = clip.volumex(0.5)

# Showing clip
clip.inpython_display(width = 280)
