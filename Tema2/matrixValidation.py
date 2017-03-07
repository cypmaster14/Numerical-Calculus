def matrixIsSimetric(matrix):
    return (matrix.transpose() == matrix).all()


def matrixIsSquared(matrix):
    matrixShape = matrix.shape  # (3, 3)
    return matrixShape[0] == matrixShape[1]


def matrixIsDiagonallyDominant(matrix):
    n = matrix[0].size
    for i in range(0, n):
        if abs(matrix[i, i]) < sum([abs(matrix[i, j]) for j in range(0, n) if i != j]):
            return False
    return True


# A matrix is positive-definite if:
#   is symmetric
#   a[i,i] >0
#   matrix is diagonally dominant
def matrixIsPositiveDefinite(matrix):
    n = matrix[0].size
    for i in range(0, n):
        if matrix[i, i] <= 0:
            return False

    # if not matrixIsDiagonallyDominant(matrix, n):
    #     return False
    return True


def matrixIsGood(matrix):
    return matrixIsSquared(matrix) and matrixIsSimetric(matrix) and matrixIsPositiveDefinite(matrix)
