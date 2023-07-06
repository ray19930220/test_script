import numpy as np
import time

# my_globals.py
thread_flag = 0
run_flag = 0
value = 48
scale = 21
lower = np.array([30, 255, 255])
upper = np.array([50, 255, 255])
image_frame_rate = 1
frame_time = 0
skill_time = 0
img = np.zeros((960, 540), dtype=np.uint8)
mask = np.zeros((960, 540), dtype=np.uint8)
hsv = np.zeros((960, 540), dtype=np.uint8)
blank_image = np.zeros((180, 180, 3), dtype=np.uint8)
drawing = False
ix, iy = -1, -1
region = (10, 30, 120, 100)
pause_flag = True
tk_img = 0