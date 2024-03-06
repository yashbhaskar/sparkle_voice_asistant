import pyautogui
import os
import time


def send_text_with_pyautogui(text):
    pyautogui.write(text)


def click():
    pyautogui.click()

os.system(r"C:\Users\ybbha\Desktop\WhatsApp.lnk")
time.sleep(1)

send_text_with_pyautogui('yash bhaskar')
time.sleep(2) 

x_coordinate = 283
y_coordinate = 234
pyautogui.moveTo(x_coordinate, y_coordinate)

click()
time.sleep(2)
send_text_with_pyautogui('Hi yash, how are you')
pyautogui.press('enter')
