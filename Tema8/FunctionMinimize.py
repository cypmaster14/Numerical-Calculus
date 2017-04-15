import numpy as np

epsilon = 1e-16
h = 10 ** -5
k_max = 10 ** 5


def get_delta_x(coefficients, x_k, x_k_prev, i):
    numarator = (x_k - x_k_prev) * approximate_first_derivatived(coefficients, x_k, i)
    numitor = approximate_first_derivatived(coefficients, x_k, i) \
              - approximate_first_derivatived(coefficients, x_k_prev, i)
    if abs(numitor) <= epsilon:
        return 10 ** -5

    return numarator / numitor


def evaluate_polynom(coefficients, value):
    return np.polyval(coefficients, value)


def approximate_first_derivatived(coefficients, x, i):
    if i == 1:
        numarator = 3 * evaluate_polynom(coefficients, x) \
                    - 4 * evaluate_polynom(coefficients, x - h) \
                    + evaluate_polynom(coefficients, x - 2 * h)
        numitor = 2 * h
        return numarator / numitor

    numarator = -evaluate_polynom(coefficients, x + 2 * h) \
                + 8 * evaluate_polynom(coefficients, x + h) \
                - 8 * evaluate_polynom(coefficients, x - h) \
                - evaluate_polynom(coefficients, x - 2 * h)
    numitor = 12 * h
    return numarator / numitor


def approximate_second_derivatived(coefficients, x):
    numarator = -evaluate_polynom(coefficients, x + 2 * h) \
                + 16 * evaluate_polynom(coefficients, x + h) \
                - 30 * evaluate_polynom(coefficients, x) \
                + 16 * evaluate_polynom(coefficients, x - h) \
                - evaluate_polynom(coefficients, x - 2 * h)
    numitor = 12 * (h ** 2)
    return numarator / numitor


def minimize_function_with_secant(coefficients, i):
    x_k = [coefficients[0], coefficients[1]]
    x = coefficients[1]
    k = 0
    condition = True
    while condition:
        print("K:{k}".format(k=k))
        delta_x = get_delta_x(coefficients, x_k[1], x_k[0], i)
        x -= delta_x
        x_k[0] = x_k[1]
        x_k[1] = x
        k += 1
        condition = abs(delta_x) >= epsilon and k <= k_max and abs(delta_x) <= 10 ** 8

    if abs(delta_x) < epsilon:
        # A solution was found
        return x
    return "Divergenta"


if __name__ == "__main__":
    coefficients = [1, -4, 3]
    minim_point = minimize_function_with_secant(coefficients, 1)
    print("x*=", minim_point)
    if minim_point != "Divergenta":
        print("F\'\'(X)>0:", approximate_second_derivatived(coefficients, minim_point))
