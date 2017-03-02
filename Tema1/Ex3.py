import numpy as np
from math import sin, pi
import time
from random import uniform
from tkinter import *


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


def solve_part1():
    errors = [[0, i] for i in range(0, 7)]

    start = time.time()
    # random_values = np.random.uniform(-np.pi / 2, np.pi / 2, 10000)
    for i in range(0, 10000):
        rv = uniform(-pi / 2, pi / 2)
        for index in range(1, 7):
            error = abs(P(index, rv) - sin(rv))
            errors[index][0] += error

    delta = time.time() - start
    errors = sorted(errors, key=lambda tup: tup[0])
    return (errors[1:7], delta)


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


def P_p2(index, x):
    if index == 1:
        return firstPolynom(x, x ** 2)
    elif index == 2:
        return secondPolynom(x, x ** 2)
    elif index == 3:
        return thirdPolynom(x, x ** 2)
    elif index == 4:
        return forthPolynom(x, x ** 2)
    elif index == 5:
        return fifthPolynom(x, x ** 2)
    elif index == 6:
        return sixthPolynom(x, x ** 2)
    else:
        return -1000000


def solve_part2():
    # random_values_100k = np.random.uniform(-np.pi / 2, np.pi / 2, 100000)

    errors_and_time_100k_p1 = [[0, 0, i] for i in range(0, 7)]
    errors_and_time_100k_p2 = [[0, 0, i] for i in range(0, 7)]

    for i in range(0, 100000):
        rv = uniform(-pi / 2, pi / 2)

        for index in range(1, 7):
            t0_p1 = time.time()
            val_p1 = P(index, rv)
            tf_p1 = time.time()
            delta_p1 = tf_p1 - t0_p1
            error1 = abs(val_p1 - sin(rv))
            errors_and_time_100k_p1[index][0] += error1
            errors_and_time_100k_p1[index][1] += delta_p1

            t0_p2 = time.time()
            val_p2 = P_p2(index, rv)
            tf_p2 = time.time()
            delta_p2 = tf_p2 - t0_p2
            error2 = abs(val_p2 - sin(rv))
            errors_and_time_100k_p2[index][0] += error2
            errors_and_time_100k_p2[index][1] += delta_p2

    errors_and_time_100k_p1 = sorted(errors_and_time_100k_p1, key=lambda tup: tup[0])
    errors_and_time_100k_p2 = sorted(errors_and_time_100k_p2, key=lambda tup: tup[0])

    return (errors_and_time_100k_p1[1:7], errors_and_time_100k_p2[1:7])


def part1_msg(errors):
    msg = ''
    for error_tuple in errors:
        msg += 'Error for P' + str(error_tuple[1]) + ' is ' + str(error_tuple[0]) + '\n'
    return msg


def part2_msg(errors_and_time_p1, errors_and_time_p2):
    msg = ''
    for i in range(0, 6):
        polynomIndex = errors_and_time_p1[i][2]
        error_p1 = errors_and_time_p1[i][0]
        time_p1 = errors_and_time_p1[i][1]
        error_p2 = errors_and_time_p2[i][0]
        time_p2 = errors_and_time_p2[i][1]

        msg += 'P' + str(polynomIndex) + ' initial: ' + 'erorr= ' + str(error_p1) + ' | ' + 'time= ' + str(
            time_p1) + '\n'
        msg += 'P' + str(polynomIndex) + ' nou:  ' + 'erorr= ' + str(error_p2) + ' | ' + 'time= ' + str(time_p2)
        msg += '\n\n'
    return msg


if __name__ == "__main__":
    root = Tk()

    root.title("Exercitiul 3")
    root.geometry("500x550")

    app = Frame(root)
    app.grid()

    title_label_part1 = Label(app, text="Partea I")
    title_label_part1.grid()
    part1 = solve_part1()
    errors_part1 = part1[0]
    delta_part1 = part1[1]
    text_part1 = "Erorile pentru cele 6 polinoame in cele 10.000 numere sunt \n\n"
    text_part1 += part1_msg(errors_part1) + "\n"
    text_part1 += "Timp total : " + str(delta_part1) + "ms\n\n"
    partea1_label = Label(app, text=text_part1)
    partea1_label.grid()

    title_label_part2 = Label(app, text="Partea II")
    title_label_part2.grid()
    part2 = solve_part2()
    errors_and_time_p1 = part2[0]
    errors_and_time_p2 = part2[1]
    text_part2 = "      Erorile si timpii pentru cele 6 polinoame (initial si imbunatatit) in 100.000 numere sunt \n\n"
    text_part2 += part2_msg(errors_and_time_p1, errors_and_time_p2) + "\n"
    partea2_label = Label(app, text=text_part2)
    partea2_label.grid()

    root.mainloop()
