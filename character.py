from cv2 import boundingRect
import pydirectinput
import random
import time
import var

def get_character_location(contours):
    if len(contours) > 0:
        x, y, w, h = boundingRect(contours[0])
        character_locate = [x, y]
        return character_locate
    else:
        var.pause_flag = False


def move_character(character_locate, countours):
    if len(countours) > 0:
        if character_locate[0] > var.value + 15:
            pydirectinput.keyDown("left")
            time.sleep(random.uniform(0.5, 1))
            pydirectinput.keyUp("left")
        elif character_locate[0] < var.value:
            pydirectinput.keyDown("right")
            time.sleep(random.uniform(0.5, 1))
            pydirectinput.keyUp("right")
