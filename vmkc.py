'''
    Project     : AutoTask-VMKC
    File        : vmkc.py
    Description : The module for the vitural mouse-keyborad control.
    Author      : lysheng (@TJ-CVRSG)
    Date        : 2024-02-01
    Version     : 1.0
'''


import ctypes
import numpy as np
import time
from PIL import Image, ImageChops, ImageGrab


DIFF_THRESHOLD = 50

MOUSEKEY_LEFT = 0
MOUSEKEY_MIDDLE = 1
MOUSEKEY_RIGHT = 2

MOUSEEVENT_LEFTDOWN = 0x2
MOUSEEVENT_LEFTUP = 0x4
MOUSEEVENT_MIDDLEDOWN = 0x20
MOUSEEVENT_MIDDLEUP = 0x40 
MOUSEEVENT_RIGHTDOWN = 0x8
MOUSEEVENT_RIGHTUP = 0x10

KEYBOARDEVENT_KEYDOWN = 0
KEYBOARDEVENT_KEYUP = 2

KEY_CODE = {    "backspace": 0x08,
                "tab": 0x09,
                "clear": 0x0C,
                "enter": 0x0D,
                "shift": 0x10,
                "ctrl": 0x11,
                "alt": 0x12,
                "pause": 0x13,
                "caps_lock": 0x14,
                "esc": 0x1B,
                "space": 0x20,
                "page_up": 0x21,
                "pgup": 0x21,
                "page_down": 0x22,
                "pgdn": 0x22,
                "end": 0x23,
                "home": 0x24,
                "left": 0x25,
                "up": 0x26,
                "right": 0x27,
                "down": 0x28,
                "+": 0xBB,
                ",": 0xBC,
                "-": 0xBD,
                ".": 0xBE,
                "/": 0xBF,
                "`": 0xC0,
                ";": 0xBA,
                "[": 0xDB,
                "\\": 0xDC,
                "]": 0xDD,
                "'": 0xDE,          }

ctypes.windll.shcore.SetProcessDpiAwareness(2)

# Convert C data type to Python
class CTypePoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]

# Visual mouse event
class mouse:
    # Single click
    def click(x, y, mouse_key):
        if mouse_key == MOUSEKEY_LEFT:
            mouse_event = [MOUSEEVENT_LEFTDOWN, MOUSEEVENT_LEFTUP]
        elif mouse_key == MOUSEKEY_MIDDLE:
            mouse_event = [MOUSEEVENT_MIDDLEDOWN, MOUSEEVENT_MIDDLEUP]
        elif mouse_key == MOUSEKEY_RIGHT:
            mouse_event = [MOUSEEVENT_RIGHTDOWN, MOUSEEVENT_RIGHTUP]

        ctypes.windll.user32.SetCursorPos(x, y)
        ctypes.windll.user32.mouse_event(mouse_event[0])
        ctypes.windll.user32.mouse_event(mouse_event[1])

    # Double click
    def double_click(x, y, mouse_key):
        mouse.click(x, y, mouse_key)
        time.sleep(0.25)
        mouse.click(x, y, mouse_key)

    # Move with mouse key down
    def move(x1, y1, x2, y2, mouse_key):
        if mouse_key == MOUSEKEY_LEFT:
            mouse_event = [MOUSEEVENT_LEFTDOWN, MOUSEEVENT_LEFTUP]
        elif mouse_key == MOUSEKEY_MIDDLE:
            mouse_event = [MOUSEEVENT_MIDDLEDOWN, MOUSEEVENT_MIDDLEUP]
        elif mouse_key == MOUSEKEY_RIGHT:
            mouse_event = [MOUSEEVENT_RIGHTDOWN, MOUSEEVENT_RIGHTUP]
        ctypes.windll.user32.SetCursorPos(x1, y1)
        ctypes.windll.user32.mouse_event(mouse_event[0])
        time.sleep(1)
        ctypes.windll.user32.SetCursorPos(x2, y2)
        time.sleep(1)
        ctypes.windll.user32.mouse_event(mouse_event[1])

# Visual keyboard event
class keyboard:
    # Press key
    def press(key, delay = 0.25):
        ctypes.windll.user32.keybd_event(key, 0, KEYBOARDEVENT_KEYDOWN, 0)
        time.sleep(delay)
        ctypes.windll.user32.keybd_event(key, 0, KEYBOARDEVENT_KEYUP, 0)
    
    # Todo : String input

# Screen-Shot on bbox(left, top, right, bottom)
def screen_grab(bbox, image_path):
    image = ImageGrab.grab(bbox)
    image.save(image_path)

# Judge if the select area is nearly the same as the standard
def brute_force_judge(image_path_std, image_path_tmp):
    image_std = Image.open(image_path_std).convert('L')
    image_tmp = Image.open(image_path_tmp).convert('L')
    image_diff = ImageChops.subtract(image_std, image_tmp)
    
    diff = np.array(image_diff)
    if diff.sum() < DIFF_THRESHOLD:
        return True
    else:
        return False
