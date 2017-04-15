from Tema8.Utils import *
from  Tema8.FunctionMinimize import approximate_first_derivatived, approximate_second_derivatived
import cmath
import numpy as np
import random


def evaluate_polynom(coefficients: list, x: complex) -> complex:
    c = x.real
    d = x.imag
    p = -2 * c
    q = c ** 2 + d ** 2
    b = [0, 0]
    b[0] = coefficients[0]
    b[1] = coefficients[1] - p * b[0]
    for i in range(2, len(coefficients)):
        b_i = coefficients[i] - p * b[1] - q * b[0]
        b[0], b[1] = b[1], b_i

    return complex(b[0] * c + b[1] + p * b[0], b[0] * d)


def get_sign(x):
    return 1 if x.real >= 0 else -1


def get_h_x(coefficients, x_k, p_first_derivatived) -> complex:
    p_second_derivatived = approximate_second_derivatived(coefficients, x_k)
    n = len(coefficients) - 1
    h_x = (n - 1) ** 2 * (p_first_derivatived ** 2)
    h_x = h_x - n * (n - 1) * evaluate_polynom(coefficients, x_k) * p_second_derivatived

    return h_x


def get_delta_x(coefficients, x_k) -> complex:
    n = len(coefficients) - 1
    p_first_derivatived = approximate_first_derivatived(coefficients, x_k, 1)

    numarator = n * evaluate_polynom(coefficients, x_k)
    h_x = get_h_x(coefficients, x_k, p_first_derivatived)
    numitor = p_first_derivatived \
              + get_sign(p_first_derivatived) * cmath.sqrt(h_x)

    if abs(numitor.real) < epsilon:
        print("[EXIT] Trebuie sa alegem alt x_0")
        return None

    return numarator / numitor


def get_polynom_complex_root_laguerre(coefficients: list, x: complex):
    k = 0
    delta_x = 0
    condition = True
    while condition:
        delta_x = get_delta_x(coefficients, x)
        if delta_x is None:
            return None
        x = x - delta_x
        k += 1

        condition = epsilon <= abs(delta_x.real) <= 10 ** 8 and k <= k_max

    if abs(delta_x.real) < epsilon:
        return x
    return None


def get_complex_roots(coefficients):
    R = getValuesInterval(coefficients)
    print(R)
    print(np.roots(coefficients))
    roots = set()
    i = 0
    while i < 1000:
        print("I:", i)
        x = complex(random.uniform(-R, R), random.uniform(-R, R))
        possible_root = get_polynom_complex_root_laguerre(coefficients, x)
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
    coefficients = [1, 1, -25, 41, 66]
    print(get_complex_roots(coefficients))
