import numpy as np
from math import sqrt
import random
from Tema8.Utils import *
from Tema8.FunctionMinimize import approximate_first_derivatived, approximate_second_derivatived


def evaluate_polynom(coefficients, x):
    b = coefficients[0]
    q_x = 0
    n = len(coefficients) - 1
    for i in range(0, n):
        q_x += b * (x ** (n - i - 1))
        b = coefficients[i + 1] + b * v

    p_x = (x - v) * q_x + b  # b_n=r=P(v)
    return p_x


def get_h_x(coefficients, x_k, p_first_derivative):
    p_second_derivative = approximate_second_derivatived(coefficients, x_k)
    n = len(coefficients) - 1

    h_x = (n - 1) ** 2 * p_first_derivative ** 2
    h_x = h_x - n * (n - 1) * evaluate_polynom(coefficients, x_k) * p_second_derivative
    if h_x < 0:
        print("[EXIT] Trebuie sa alegem alt x_0")
        return None

    return h_x


def get_sign(x):
    return 1 if x >= 0 else -1


def get_delta_x(coefficients, x_k):
    n = len(coefficients) - 1
    p_first_derivative = approximate_first_derivatived(coefficients, x_k, 1)

    numarator = n * evaluate_polynom(coefficients, x_k)
    numitor = p_first_derivative
    h_x = get_h_x(coefficients, x_k, p_first_derivative)
    if h_x is None:
        return None
    numitor = numitor + get_sign(numitor) * sqrt(h_x)
    if abs(numitor) <= epsilon:
        print("[EXIT] Trebuie sa alegem alt x_0")
        return None

    return numarator / numitor


def get_polynom_root_laguerre(coefficients, x):
    k = 0
    delta_x = 0
    condition = True
    while condition:
        delta_x = get_delta_x(coefficients, x)
        if delta_x == None:
            return None
        x = x - delta_x
        k += 1
        condition = epsilon <= abs(delta_x) <= 10 ** 8 and k < k_max

    if abs(delta_x) < epsilon:
        return x
    return None


def get_real_roots(coefficients):
    R = getValuesInterval(coefficients)
    print(R)
    print(np.roots(coefficients))
    roots = set()
    i = 0
    while i < 1000:
        print("I:", i)
        x = random.uniform(-R, R)
        possible_root = get_polynom_root_laguerre(coefficients, x)
        if possible_root is not None:
            add = True
            for value in roots:
                if abs(value - possible_root) < epsilon:
                    add = False
                    break
            if add:
                roots.add(possible_root)
        i += 1
    return roots


if __name__ == "__main__":
    coefficients = [1, -6, 11, -6]
    print(get_real_roots(coefficients))
