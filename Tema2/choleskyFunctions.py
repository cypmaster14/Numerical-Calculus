import numpy


def choleskyDecomposition(A, d, e):
    n = A[0].size
    for p in range(0, n):

        # d[p] computation
        d[p] = A[p, p] - sum(d[k] * (A[p, k] ** 2) for k in range(0, p))

        # l[i][p] computation
        for i in range(p + 1, n):
            value = sum(d[k] * A[i, k] * A[p, k] for k in range(0, p))
            if abs(d[p]) > e:
                A[i, p] = (A[i, p] - value) / d[p]
            else:
                print('Impartirea nu poate avea loc')
                exit()


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
