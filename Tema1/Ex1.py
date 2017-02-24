from tkinter import *


def compute_u():
    m = -1
    u = 10
    while 1.0 + u != 1.0:
        u = 10 ** m
        m -= 1
    return u


if __name__ == "__main__":
    root = Tk()

    root.title("Exercitiul 1")
    root.geometry("230x200")

    app = Frame(root)
    app.grid()
    label = Label(app, text="Precizia masina este u = " + str(compute_u()))
    label.grid()
    root.mainloop()
