import time
import pyautogui
from pynput.mouse import Controller

def play(proc):
    pyautogui.FAILSAFE = False
    with open("data", "r") as file:
        lines = file.readlines()
        i = 0
        for l in lines:
            line = l.replace("\n", "")
            i += 1
            if i%2 != 0:
                print(f"WAITING FOR {str(int(float(l)))} SECONDS")
                time.sleep(int(float(line)))
            elif i%2 == 0 and len(line.split(" ")) == 3 or 4:
                x = int(line.split(" ")[0])
                y = int(line.split(" ")[1])
                if "RIGHT" in line.split(" "):
                    print(f"RIGHT CLICKED AT {x}, {y}")
                    pyautogui.click(x, y, button='right')
                if "LEFT" in line.split(" "):
                    print(f"LEFT CLICKED AT {x}, {y}")
                    pyautogui.click(x, y, button='left')
                if "SCROLL" in line.split(" "):
                    dx = int(line.split(" ")[2])
                    dy = int(line.split(" ")[3])
                    print(f"SCROLLED {'down' if dy < 0 else 'up'} FROM {x}, {y}")
                    pyautogui.moveTo(x, y)
                    Controller().scroll(dx, dy)