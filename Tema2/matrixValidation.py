def matrixIsSimetric(matrix):
    return (matrix.transpose() == matrix).all()


def matrixIsSquared(matrix):
    matrixShape = matrix.shape  # (3, 3)
    return matrixShape[0] == matrixShape[1]


def matrixIsPossitiveDefinite(matrix, n):
    return True


def matrixIsGood(matrix, n):
    return matrixIsSquared(matrix) and matrixIsSimetric(matrix) and matrixIsPossitiveDefinite(matrix, n)
