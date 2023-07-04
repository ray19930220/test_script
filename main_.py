import cv2
import numpy as np
import pyautogui
import pydirectinput
import time
import var
import sys
import win32gui
import random
from character import get_character_location, move_character
from display import display_images, puttext
from tkinter import *
from tkinter.ttk import *


def take_screenshot():
    screenshot = pyautogui.screenshot(region=var.region)
    screenshot.save("./Picture/screenshot.png")
    return cv2.imread("./Picture/screenshot.png")


# main
def do_something():
    print(time.time())
    if not pause_flag:
        var.img = take_screenshot()
        var.hsv = cv2.cvtColor(var.img, cv2.COLOR_BGR2HSV)
        var.mask = cv2.inRange(var.hsv, var.lower, var.upper)
        contours, _ = cv2.findContours(
            var.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        # character position
        character_locate = get_character_location(contours)
        move_character(character_locate, contours)
        # skill
        if time.time() >= (var.skill_time + 5):
            execute_skill("t")

        puttext()
        root.after(100000, do_something)


def get_window_handle(window_title):
    handle = win32gui.FindWindow(None, window_title)
    return handle


def switch_to_window(window_handle):
    # 將焦點切換到指定的窗口
    win32gui.SetForegroundWindow(window_handle)


def pause_execution():
    global pause_flag
    pause_flag = True
    label.config(text="暫停")


def start_execution():
    global pause_flag
    pause_flag = False
    label.config(text="執行中")
    do_something()


def exit_execution():
    sys.exit()


# for skill press
def execute_skill(skill_btn):
    print(skill_btn, end="press \n")
    # pydirectinput.press(skill_btn)
    time.sleep(random.uniform(3, 3.5))
    var.skill_time = time.time()


def show_origin_image():
    if origin_image_on.get():
        display_images("origin_image", var.img)


def show_filter_image():
    if filter_image_on.get():
        display_images("filter_image", var.hsv)


# for GUI

root = Tk()
origin_image_on = IntVar()
filter_image_on = IntVar()

label = LabelFrame(root, text="請按開始...")
label.pack()
# 創建一個按鈕，當按下時執行do_something函數
button = Button(root, text="開始", command=start_execution)
button.pack()

# 創建一個結束按鈕，當按下時執行pause_execution函數
pause_button = Button(root, text="暫停", command=pause_execution)
pause_button.pack()

origin_image_button = Checkbutton(
    root,
    text="顯示原始影像",
    variable=origin_image_on,
    onvalue=1,
    offvalue=0,
    command=show_origin_image,
)
origin_image_button.pack()

filter_image_button = Checkbutton(
    root,
    text="顯示慮波影像",
    variable=filter_image_on,
    onvalue=1,
    offvalue=0,
    command=show_filter_image,
)
filter_image_button.pack()

end_button = Button(root, text="結束", command=exit_execution)
end_button.pack()

# 設置停止標誌的初始值
pause_flag = True
root.geometry("+1600+720")
# 啟動Tkinter的事件循環
root.mainloop()
