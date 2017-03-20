import Tema2.system as system
from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.geometry("700x700+300+300")
    system = system.System('input.json', root)
    root.mainloop()
    # system.doSomething()
