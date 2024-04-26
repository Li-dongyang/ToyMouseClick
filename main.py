from pynput.mouse import Button, Controller
import keyboard
import time

CPS = 25 # click per second

clicking = False

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print('clicking ...', flush=True)
    else:
        print('... inactive', flush=True)

mouse = Controller()
# mouse.position = (10, 20) 设置鼠标位置
keyboard.add_hotkey('F9', toggle_clicking) # this is a callback function

while True:
    if clicking:
        mouse.click(Button.left, 1) # 单击
        time.sleep(1.0 / CPS)
