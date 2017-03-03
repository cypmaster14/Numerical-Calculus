import numpy


def choleskyDecomposition(A, d, n):
    for p in range(0, n):

        # d[p] computation
        d[p] = A[p, p]
        for k in range(0, p):
            d[p] -= d[k] * (A[p, k] ** 2)

        # l[i][p] computation

        for i in range(p + 1, n):
            value = 0
            for k in range(0, p):
                value += d[k] * A[i, k] * A[p, k]
            A[i, p] = (A[i, p] - value) / d[p]


# A=LDT(d)
# det(A)=det(L)*det(D)*det(T(l)
# det(L)=det(T(l))=1
# => det(A)=det(D)
def choeleskyDeterminant(d):
    return d.prod()


def choleskyLUDecomposition(A):
    L = numpy.linalg.cholesky(A)
    U = L.transpose()
    return L, U
