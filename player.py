import time
import pyautogui

def play():
    pyautogui.FAILSAFE = False
    with open("data", "r") as file:
        lines = file.readlines()
        i = 0
        for l in lines:
            line = l.replace("\n", "")
            i += 1
            if i%2 != 0:
                print(f"WAITING FOR {str(int(float(l)))} SECONDS")
                time.sleep(float(line))
            elif i%2 == 0 and len(line.split(" ")) == 2:
                x = int(line.split(" ")[0])
                y = int(line.split(" ")[1])
                print(f"CLICKED AT {x}, {y}")
                pyautogui.move(x, y)
                pyautogui.click(x, y)