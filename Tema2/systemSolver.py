import numpy


def solveSystem(A, d, n, b):
    # Solve the first system L*z=b
    z = numpy.zeros(n)
    for i in range(0, n):
        z[i] = b[i]
        for j in range(0, i):
            z[i] -= A[i, j] * z[j]

    # Solve the second system D*y=z
    y = numpy.zeros(n)
    for i in range(0, n):
        y[i] = z[i] / d[i]

    # Solve the third system

    x = numpy.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= A[j, i] * x[j]

    return x


def solveSystemClasically(A, b):
    x = numpy.linalg.solve(A, b)
    return x
