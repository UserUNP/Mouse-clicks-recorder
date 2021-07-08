from multiprocessing import Process
from pynput import mouse
import player
import frame
import time
import os

oldClickTime = time.time()
proc = None

def on_click(x, y, button, pressed):
    global oldClickTime
    if button == mouse.Button.left and pressed:
        start = time.time()
        print(f"Registered {x}, {y}.")
        with open("data", "a") as file:
            file.write(f"{str(start - oldClickTime)}\n")
        with open("data", "a") as file:
            file.write(f"{x} {y}\n")
        start = time.time()
        oldClickTime = time.time()


def startlisten():
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()

def startplay():
    player.play()

def PLAY():
    global proc
    if proc != None:
        print("Cannot start more than one thread")
        frame.error("Cannot start more than one thread")
        return
    else:
        proc = Process(target=startplay)
        proc.start()

def START():
    global proc
    if proc != None:
        print("Cannot start more than one thread")
        frame.error("Cannot start more than one thread")
        return
    else:
        if "data" in os.listdir():
            os.remove("data")
        proc = Process(target=startlisten)
        proc.start()
def STOP():
    global proc
    if proc!=None:
        proc.terminate()
        proc = None

def onquit():
    STOP()
    window.get().destroy()

if __name__ == "__main__":
    window = frame.new_frame("LEFT CLICK RECORDER", 157, 50, False)
    window.get().protocol("WM_DELETE_WINDOW", onquit)
    window.button("Start", 10, 15, START)
    window.button("Stop", 50, 15, STOP)
    window.button("Playback", 90, 15, PLAY)
    window.get().mainloop()