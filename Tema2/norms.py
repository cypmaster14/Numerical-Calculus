import numpy
from math import sqrt


def getSecondNorm(A, x, b):
    # Compute y=A(init) *x
    n = A[0].size
    y = numpy.zeros(n)
    for i in range(0, n):
        for j in range(0, n):
            if i > j:
                y[i] += A[j, i] * x[j]
            else:
                y[i] += A[i, j] * x[j]

    # Compute z=y-b
    z = numpy.subtract(y, b)

    # Compute the euclidean norm
    eucledianNorm = sum(z[i] ** 2 for i in range(0, n))
    return sqrt(eucledianNorm)
