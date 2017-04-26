from numpy.random import uniform
from numpy import sort
from numpy import append
from numpy import pi
import Functions
import Aitken
import Trigonometry
import matplotlib.pyplot as matplot


def get_Xs():
    with open("input.txt") as f:
        x0, xn, n = [int(z) for z in next(f).split()]
    x = uniform(x0,xn,n-1)
    x = append(x,x0)
    x = append(x,xn)
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
    for i in range(0,n+1):
        approx_f.append(Aitken.Ln(n,x,f,x[i]))
    return approx_f


def get_approx_f_trigonometry(n, x, f):
    approx_f = []
    for i in range(0,n+1):
        approx_f.append(Trigonometry.solve(n,x,f,x[i]))
    return approx_f


def draw_plot_aitken(x,f,approx_f):
    matplot.plot(x,f,'r--',x,approx_f,'b--')
    matplot.ylabel('Aitken')
    matplot.show()


def draw_plot_trigonometry(x,f,approx_f):
    matplot.plot(x,f,'r--',x,approx_f,'b--')
    matplot.ylabel('Trigonometry')
    matplot.show()


def main_aitken():
    x = get_Xs()
    f = get_Fs1(x)
    n = len(x) - 1
    x_new = 6
    approx_fx = Aitken.Ln(n,x,f,x_new)
    print "Ln(x) = " + str(approx_fx)
    print "|Ln(x)-f(x)| = " + str(abs(approx_fx - Functions.f1(x_new)))
    approx_f = get_approx_f_aitken(n,x,f)
    draw_plot_aitken(x,f,approx_f)


def main_trigonometry():
    x = get_Xs()
    f = get_Fs2(x)
    n = len(x) - 1
    x_new = pi/13+1
    approx_fx = Trigonometry.solve(n, x, f, x_new)
    print "Tn(x) = " + str(approx_fx)
    print "|Tn(x)-f(x)| = " + str(abs(approx_fx - Functions.f2(x_new)))
    approx_f = get_approx_f_trigonometry(n,x,f)
    draw_plot_trigonometry(x,f,approx_f)


main_aitken()
main_trigonometry()
