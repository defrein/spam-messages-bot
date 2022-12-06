import pyautogui
import time

time.sleep(3)  # time for change your cursor position
position = pyautogui.position()
messages = "Hello World"
for a in range(10):
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(messages)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])
