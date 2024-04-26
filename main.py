from pynput.mouse import Button, Controller
import keyboard
import time

clicking = False

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print('clicking ---', flush=True)

mouse = Controller()
# mouse.position = (10, 20) 设置鼠标位置
keyboard.add_hotkey('F9', toggle_clicking) # this is a callback function
# keyboard.add_hotkey('F10', toggle_clicking)

while True:
    if clicking:
        mouse.click(Button.left, 1) # 单击
        time.sleep(0.05)  # 控制点击速度
