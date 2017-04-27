from numpy.random import uniform
from numpy import sort
from numpy import append
from numpy import pi
import Tema7.Functions as Functions
import Tema7.Aitken as Aitken
import Tema7.Trigonometry as Trigonometry
import matplotlib.pyplot as matplot
from tkinter import *

root = Tk()
text = Text()


def get_Xs():
    with open("input.txt") as f:
        x0, xn, n = [int(z) for z in next(f).split()]
    x = uniform(x0, xn, n - 1)
    x = append(x, x0)
    x = append(x, xn)
    x = sort(x)
    x = x.tolist()
    return x


def get_Fs1(x):
    f = []
    for xi in x:
        f.append(Functions.f1(xi))
    return f


def get_Fs2(x):
    f = []
    for xi in x:
        f.append(Functions.f2(xi))
    return f


def get_approx_f_aitken(n, x, f):
    approx_f = []
    for i in range(0, n + 1):
        approx_f.append(Aitken.Ln(n, x, f, x[i]))
    return approx_f


def get_approx_f_trigonometry(n, x, f):
    approx_f = []
    for i in range(0, n + 1):
        approx_f.append(Trigonometry.solve(n, x, f, x[i]))
    return approx_f


def draw_plot_aitken(x, f, approx_f):
    matplot.plot(x, f, 'r--', x, approx_f, 'b--')
    matplot.ylabel('Aitken')
    matplot.show()


def draw_plot_trigonometry(x, f, approx_f):
    matplot.plot(x, f, 'r--', x, approx_f, 'b--')
    matplot.ylabel('Trigonometry')
    matplot.show()


def main_aitken():
    x = get_Xs()
    f = get_Fs1(x)
    n = len(x) - 1
    x_new = 6
    approx_fx = Aitken.Ln(n, x, f, x_new)
    print("Ln(x) = " + str(approx_fx))
    print("|Ln(x)-f(x)| = " + str(abs(approx_fx - Functions.f1(x_new))))
    text.insert(INSERT,
                "Ln(x) = {}\n|Ln(x)-f(x)| = {}\n".format(str(approx_fx), str(abs(approx_fx - Functions.f1(x_new)))))

    approx_f = get_approx_f_aitken(n, x, f)
    draw_plot_aitken(x, f, approx_f)


def main_trigonometry():
    x = get_Xs()
    f = get_Fs2(x)
    n = len(x) - 1
    x_new = pi / 13 + 1
    approx_fx = Trigonometry.solve(n, x, f, x_new)
    print("Tn(x) = " + str(approx_fx))
    print("|Tn(x)-f(x)| = " + str(abs(approx_fx - Functions.f2(x_new))))
    text.insert(INSERT,
                "Tn(x) = {}\n|Tn(x)-f(x)| = {}\n".format(str(approx_fx), str(abs(approx_fx - Functions.f2(x_new)))))
    approx_f = get_approx_f_trigonometry(n, x, f)
    draw_plot_trigonometry(x, f, approx_f)


def initUi(parent):
    global text

    frame1 = Frame(parent)
    frame1.pack(fill=X)

    buttonAitken = Button(frame1, text="Aitken", width=10, command=main_aitken)
    buttonAitken.pack(padx=5, pady=5)

    buttonTrigonometry = Button(frame1, text="Trigonometry", width=12, command=main_trigonometry)
    buttonTrigonometry.pack(padx=5, pady=5)

    frame2 = Frame(parent)
    frame2.pack(fill=X)

    text = Text(frame2, height=200, width=900)
    text.pack(padx=5, pady=5)


if __name__ == "__main__":
    root.geometry("900x700+300+300")
    initUi(root)
    root.mainloop()
