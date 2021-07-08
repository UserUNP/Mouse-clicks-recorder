from tkinter import *
###############

class new_frame():
    def __init__(self, title:str, width:int, height:int, resizable:bool):
        global window
        window = Tk()
        window.title(title)
        window.geometry(f"{width}x{height}")
        if resizable==False:
            window.resizable(False, False)
    def get(self):
        return window
    def label(self, l:str, posx:int, posy:int, **kwargs):
        color = kwargs.get("color", None)
        font = kwargs.get("font", None)
        if color==None and font==None:
            lbl = Label(window, text=l)
            lbl.place(x=posx, y=posy)
        elif color!=None and font==None:
            lbl = Label(window, text=l, fg=color)
            lbl.place(x=posx, y=posy)
        elif font!=None and color==None:
            lbl = Label(window, text=l, font=font)
            lbl.place(x=posx, y=posy)
        else:
            lbl = Label(window, text=l, fg=color, font=font)
            lbl.place(x=posx, y=posy)
        return lbl
    def button(self, l:str, posx:int, posy:int, cmd):
        btn = Button(window, text=l, command=cmd).place(x=posx, y=posy)
        return btn
    def options(self, l:str, posx:int, posy:int, options):
        option = StringVar(window)
        option.set(l)
        OptionMenu(window, option, *options).place(x=posx, y=posy)
        return option
    def text(self, posx:int, posy:int, w:int, h:int, **kwargs):
        disabled = kwargs.get("disabled")
        if disabled==True:
            txt = Text(window, width=w, height=h)
            txt.configure(state="disabled")
            txt.place(x=posx, y=posy)
        else:
            txt = Text(window, width=w, height=h)
            txt.place(x=posx, y=posy)
        return txt
    def entry(self, l:str, posx:int, posy:int, w:int, h:int):
        entr = Entry(window, text=l)
        entr.place(x=posx, y=posy, width=w, height=h)
        return entr

def error(text:str):
    popup = Tk()
    popup.title("Error!")
    Label(popup, text = text, font = ("Verdana", 12)).pack()
    popup.geometry(f'{len(text)*10}x50')
    popup.resizable(False, False)
    popup.mainloop()
    return popup