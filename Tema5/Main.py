from Tema5.IterativeInverse import IterativeInverse
import numpy as np
from tkinter import *
import tkinter.messagebox as messagebox

root = Tk()
lbl1 = Label(root)
lbl2 = Label(root)
text = Text()


def compute_epsilon():
    m = -1
    u = 10
    while 1.0 + u != 1.0:
        u = 10 ** m
        m -= 1
    return u


def button_click():
    text.delete('1.0', END)
    main()


def initUi(parent):
    parent.title("Tema 5")
    global lbl1, lbl2, text

    frame1 = Frame(parent)
    frame1.pack(fill=X)

    lbl1 = Label(frame1, text="Norma:", width=30)
    lbl1.pack(side=LEFT, padx=5, pady=5)

    lbl2 = Label(frame1, text="Iteratii:", width=30)
    lbl2.pack(side=LEFT, padx=5, pady=5)

    button = Button(frame1, text="Calculate", width=10, command=button_click)
    button.pack(padx=5, pady=5)

    frame2 = Frame(parent)
    frame2.pack(fill=X)

    text = Text(frame2, height=200, width=900)
    text.pack(padx=5, pady=5)


def main():
    a = []
    with open("matrix.txt") as f:
        n = int(next(f))
        for line_s in f:  # read rest of lines
            line = [int(x) for x in line_s.split(" ")]
            a.append(line)
    a = np.array(a)
    ii = IterativeInverse(n, compute_epsilon(), 1000, a)
    result = ii.solve(3)
    if len(result) == 1:
        messagebox.showinfo("Error", "Matrix is divergent")
    else:
        print("Result:", result)
        lbl1['text'] = "Norm:" + str(result[0])
        lbl2['text'] = "Iterations:" + str(result[1])
        text.insert(INSERT, "Inverse:\n{}\nNumpyInverse:\n{}".format(result[2], result[3]))


if __name__ == "__main__":
    root.geometry("900x700+300+300")
    initUi(root)
    root.mainloop()
