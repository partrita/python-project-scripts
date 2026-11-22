import time

import pyautogui

with open('text', 'r') as text:
    time.sleep(5)

    for word in text:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(5)