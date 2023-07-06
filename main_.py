import cv2
import numpy as np
import pyautogui
import pydirectinput
import time
import var
import sys
import win32gui
import random
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from character import get_character_location, move_character
from display import display_images


def take_screenshot():
    screenshot = pyautogui.screenshot(
        region=(
            capture_region.winfo_x(),
            capture_region.winfo_y(),
            capture_region.winfo_width(),
            capture_region.winfo_height(),
        )
    )
    screenshot.save("./screenshot.png")
    return cv2.imread("./screenshot.png")


# main
def main_run():
    if var.run_flag:
        if time.time() >= (var.frame_time + (1 / var.image_frame_rate)):
            print("take_screenshot")
            var.img = take_screenshot()
            var.tk_img = ImageTk.PhotoImage(Image.open("./screenshot.png"))
            canvas.create_image(0, 0, image=var.tk_img, anchor="nw")
            var.hsv = cv2.cvtColor(var.img, cv2.COLOR_BGR2HSV)
            var.mask = cv2.inRange(var.hsv, var.lower, var.upper)
            contours, _ = cv2.findContours(
                var.mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            # character position
            # character_locate = get_character_location(contours)
            # move_character(character_locate, contours)
            # skill
            # if time.time() >= (var.skill_time + 5):
            #   execute_skill("t")
            # puttext()
    root.after(200, main_run)


def get_window_handle(window_title):
    handle = win32gui.FindWindow(None, window_title)
    return handle


def switch_to_window(window_handle):
    # 將焦點切換到指定的窗口
    win32gui.SetForegroundWindow(window_handle)


def start_execution():
    var.run_flag = True
    label.config(text="執行中")
    if not var.thread_flag:
        main_run()
        var.thread_flag = 1


def pause_execution():
    var.run_flag = False
    label.config(text="暫停")


def exit_execution():
    sys.exit()


# for skill press
def execute_skill(skill_btn):
    print(skill_btn, end="press \n")
    # pydirectinput.press(skill_btn)
    time.sleep(random.uniform(3, 3.5))
    var.skill_time = time.time()


def hide_capture_region():
    if hide_capture.get():
        capture_region.attributes("-alpha", 0)
    else:
        capture_region.attributes("-alpha", 0.5)



def capture_image_resize():
    image_viewer.geometry(f'{capture_region.winfo_width()}x{capture_region.winfo_height()}')


### for GUI ###

# root window
root = Tk()
hide_capture = IntVar()
show_image = IntVar()
# info label
label = LabelFrame(root, text="請按開始...")
label.pack(fill="x")
# show capture region
hide_capture_ckb = Checkbutton(
    root,
    text="隱藏擷取範圍",
    variable=hide_capture,
    onvalue=1,
    offvalue=0,
    command=hide_capture_region,
)
hide_capture_ckb.pack()
# start btn
button = Button(root, text="開始", command=start_execution)
button.pack(fill="x")
# pause btn
pause_button = Button(root, text="暫停", command=pause_execution)
pause_button.pack(fill="x")
# capture_image_resize
capture_image_resize_button = Button(
    root,
    text="重設擷取影像大小",
    command=capture_image_resize,
)
capture_image_resize_button.pack(fill="x")
# end btn
end_button = Button(root, text="結束", command=exit_execution)
end_button.pack(fill="x")


# capture region window
capture_region = Toplevel(root)
capture_region.attributes("-alpha", 0.5)
capture_region.attributes("-topmost",True)
capture_region.geometry("300x300")
capture_region.title("capture_region")


# image viewer window
image_viewer = Toplevel(root, highlightthickness=0)
image_viewer.title("image")
image_viewer.geometry("300x300")
canvas = Canvas(image_viewer)
canvas.pack(fill="both", expand=True)


# 設置停止標誌的初始值
pause_flag = True
root.geometry("+1600+720")
# 啟動Tkinter的事件循環
root.mainloop()
