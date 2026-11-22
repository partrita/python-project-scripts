import time

import pyautogui

count = 0
pyautogui.click(10,5)
while True:
    pyautogui.FAILSAFE=True
    pyautogui.write("Hey you there")
    count +=1
    pyautogui.press("ENTER")
    time.sleep(1)