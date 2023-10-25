import pyautogui
import threading
import random
# print(pyautogui.position())
# pyautogui.click(1465,747)
# pyautogui.click(1087,697)

# pyautogui.moveTo(1465,747,1)
# pyautogui.click()

# pyautogui.moveTo(1087,697, 1)
# pyautogui.click()

# pyautogui.moveTo(1407,540, 1)
# pyautogui.click()

# 1465 747
# #1097 697
# 1407 540

def test():
    # pyautogui.moveTo(1465,747,1)
    pyautogui.click()
    pyautogui.click()

def set_interval(func):
    sec = random.uniform(59, 59.7)
    print(sec)
    def func_wrapper():
        set_interval(func)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

print(set_interval(test))
#             python main.py