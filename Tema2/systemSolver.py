import numpy


def solveSystem(A, d, b):
    # Solve the first system L*z=b
    n = A[0].size
    z = numpy.zeros(n, dtype=numpy.float_)
    for i in range(0, n):
        z[i] = b[i] - sum(A[i, j] * z[j] for j in range(0, i))

    # Solve the second system D*y=z
    y = numpy.zeros(n, dtype=numpy.float_)
    for i in range(0, n):
        y[i] = z[i] / d[i]

    # Solve the third system

    x = numpy.zeros(n, dtype=numpy.float_)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(A[j, i] * x[j] for j in range(i + 1, n))

    return x


def solveSystemClasically(A, b):
    x = numpy.linalg.solve(A, b)
    return x
