import numpy
from math import sqrt


def getSecondNorm(A, x, b, n):
    # Compute y=A(init) *x

    y = numpy.zeros(n)
    for i in range(0, n):
        for j in range(0, n):
            if i > j:
                y[i] += A[j, i] * x[j]
            else:
                y[i] += A[i, j] * x[j]

    # Compute z=y-b
    z = numpy.subtract(y, b)

    # Compute the eucledian norm
    eucledianNorm = 0
    for i in range(0, n):
        eucledianNorm += z[i] ** 2

    return sqrt(eucledianNorm)
