v = 3
epsilon = 1e-15
k_max = 10 ** 6


def get_derivative_polynom(coefficients: list) -> list:
    derivative_polynom = []
    for i in range(0, len(coefficients) - 1):
        derivative_polynom.append(coefficients[i] * (len(coefficients) - i - 1))
    return derivative_polynom


def getValuesInterval(coefficients):
    A = abs(max(coefficients, key=lambda x: abs(x)))
    R = (abs(coefficients[0]) + A) / abs(coefficients[0])
    return R
