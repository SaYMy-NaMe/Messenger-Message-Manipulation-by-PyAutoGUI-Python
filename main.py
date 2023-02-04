import pyautogui
import time
value = int(input())
for i in range(value):
    pyautogui.sleep(3)
    pyautogui.typewrite("Hey Brother")
    pyautogui.sleep(2)
    pyautogui.press('return')
#Keep the cursur where you wanna text
