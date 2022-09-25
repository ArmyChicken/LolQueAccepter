from pyautogui import *
import pyautogui
import time
# import win32api, win32con

# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#     time.sleep(0.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#infinite loop checks if logo.png appears on screen it clicks it
while 1:
    if pyautogui.locateOnScreen("loko.png", region=(), grayscale=True, confidence=0.8) != None:
        click(957, 744)      
        exit()
    else:
        print("Challenger kjů lol")
        time.sleep(0.5)
