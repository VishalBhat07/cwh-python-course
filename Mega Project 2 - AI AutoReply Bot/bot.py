from response import AIprocess
from main import content
import pyautogui
import pyperclip
import time

x, y = (957, 957)

chat_history = content()
reply = AIprocess(chat_history)

time.sleep(2)

pyautogui.moveTo(x, y)
pyautogui.click(x, y)

time.sleep(0.5)

pyperclip.copy(reply)

time.sleep(0.5)

pyautogui.hotkey('ctrl', 'v')

# pyautogui.click('enter')
print(reply)
