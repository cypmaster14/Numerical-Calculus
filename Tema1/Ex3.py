import numpy as np
from math import sin, pi
import time
from random import uniform


def inv_fact(n):
    sol = 1.0
    for i in range(2, n + 1):
        sol = sol * 1 / i
    return sol


def compute_c1():
    return inv_fact(3)


def compute_c2():
    return inv_fact(5)


def compute_c3():
    return inv_fact(7)


def compute_c4():
    return inv_fact(9)


def compute_c5():
    return inv_fact(11)


def compute_c6():
    return inv_fact(13)


c = [0, compute_c1(), compute_c2(), compute_c3(), compute_c4(), compute_c5(), compute_c6()]


def P1(x):
    x_3 = x ** 3
    x_5 = x ** 5
    return x - c[1] * x_3 + c[2] * x_5


def P2(x):
    x_7 = x ** 7
    return P1(x) - c[3] * x_7


def P3(x):
    x_9 = x ** 9
    return P2(x) + c[4] * x_9


def P4(x):
    x_3 = x ** 3
    x_5 = x ** 5
    x_7 = x ** 7
    x_9 = x ** 9
    return x - 0.166 * x_3 + 0.00833 * x_5 - c[3] * x_7 + c[4] * x_9


def P5(x):
    x_11 = x ** 11
    return P3(x) - c[5] * x_11


def P6(x):
    x_13 = x ** 13
    return P5(x) + c[6] * x_13


def P(index, x):
    if index == 1:
        return P1(x)
    elif index == 2:
        return P2(x)
    elif index == 3:
        return P3(x)
    elif index == 4:
        return P4(x)
    elif index == 5:
        return P5(x)
    elif index == 6:
        return P6(x)
    else:
        return -1000000


errors = [[0, i] for i in range(0, 7)]

start = time.time()
random_values = np.random.uniform(-np.pi / 2, np.pi / 2, 10000)

for rv in random_values:
    for index in range(1, 7):
        error = abs(P(index, rv) - sin(rv))
        errors[index][0] += error
print(time.time() - start)
errors = sorted(errors, key=lambda tup: tup[0])
print(errors[1:7])


# Part 2
def firstPolynom(x, y):
    return x * (1 - y * (c[1] - y * c[2]))


def secondPolynom(x, y):
    return x * (1 - y * (c[1] - y * (c[2] - y * c[3])))


def thirdPolynom(x, y):
    return x * (1 - y * (c[1] - y * (c[2] - y * (c[3] - y * c[4]))))


def forthPolynom(x, y):
    return x * (1 - y * (0.166 - y * (0.00833 - y * (c[3] - y * c[4]))))


def fifthPolynom(x, y):
    return x * (1 - y * (c[1] - y * (c[2] - y * (c[3] - y * (c[4] - y * c[5])))))


def sixthPolynom(x, y):
    return x * (1 - y * (c[1] - y * (c[2] - y * (c[3] - y * (c[4] - y * (c[5] - y * c[6]))))))


