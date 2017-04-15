from Tema3.SparseMatrix import SparseMatrix
import random
import numpy as np
from Tema4.BiCGSTAB import multiply_vector

k_max = 10 ** 6
np.set_printoptions(threshold=np.inf)


def read_values(filename):
    with open(filename) as f:
        n = int(f.readline())
        b = list()
        f.readline()
        # for i in range(0, n):
        #     v = f.readline()
        #     b.append(float(v))
        # f.readline()
        matrix = f.read()
        lines = matrix.split("\n")
        del lines[-1]
        data = []
        for line in lines:
            values = line.split(',')
            data.append((float(values[0]), int(values[1]), int(values[2])))
        return (n, b, data)


def transform(n, elements, matrix_name):
    nn_count = [0] * 100  # not null count , un vector de frecventa ce contorizeaza numarul de nn de le fiecare linie
    d = [0] * n
    hash_map = {i: [] for i in range(0, n)}
    hash_map_2 = {i: [] for i in range(0, n)}
    for element in elements:
        v = element[0]
        i = element[1]
        j = element[2]
        if i == j:
            d[i] = v
        else:
            line_elements = hash_map.get(i)
            found = False
            for line_element in line_elements:
                if line_element[1] == j:
                    line_element[0] += v
                    found = True
                    break
            if not found:
                line_elements.append([v, j])

            line_elements = hash_map_2.get(j)
            found = False
            for line_element in line_elements:
                if line_element[1] == i:
                    line_element[0] += v
                    found = True
                    break
            if not found:
                line_elements.append([v, i])

    val_col = []
    val_col_t = []
    for line in range(0, n + 1):
        val_col.append((0, -line))
        line_elements = hash_map.get(line)
        if line_elements is not None:
            for (val, col) in line_elements:
                val_col.append((val, col))

        val_col_t.append((0, -line))
        line_elements = hash_map_2.get(line)
        if line_elements is not None:
            for (val, col) in line_elements:
                val_col_t.append((val, col))

    return (d, val_col, val_col_t)


def matrixes_are_equal(A, B):
    if A.n != B.n:
        return False
    if len(A.val_col) != len(B.val_col) or len(A.d) != len(B.d):
        return False
    for i in range(0, A.n):
        if A.d[i] != B.d[i]:
            return False
    A_sorted = sorted(A.val_col, key=lambda tup: (round(tup[0], 10), tup[1]))
    B_sorted = sorted(B.val_col, key=lambda tup: (round(tup[0], 10), tup[1]))
    epsilon = 1e-9
    for i in range(0, len(A_sorted)):
        if abs(A_sorted[i][0] - B_sorted[i][0]) > epsilon or A_sorted[i][1] != B_sorted[i][1]:
            print("I:", i)
            return False
    return True


def read_matrix(filename):
    matrix_name = filename.split(".")[0].upper()
    matrix_data = read_values(filename)
    n = matrix_data[0]
    b = matrix_data[1]
    matrix_d, matrix_val_col, matrix_val_col_t = transform(n, matrix_data[2], matrix_name)
    M = SparseMatrix(n, matrix_d, matrix_val_col, matrix_name)
    M_T = SparseMatrix(n, matrix_d, matrix_val_col_t, matrix_name)
    M.isSymetric = matrixes_are_equal(M, M_T)
    print("A=A_T ??", M.isSymetric)
    print(matrix_name + " diagonals (first 10) = " + str(M.d[0:10]))
    print(matrix_name + " val_col (first 10) = " + str(M.val_col[0:10]))
    return M


def firstMethod(p, n, matrixName):
    generatedMatrix = generateSparseMatrix(p, n)
    fileMatrix = read_matrix(matrixName)
    return generatedMatrix, fileMatrix


def generateSparseMatrix(p, n):
    values = {i: [] for i in range(0, p)}
    diag = list()
    for line in range(0, p):
        numberOfValues = random.randint(0, 9)
        diag.append(random.randint(0, 30))
        j = len(values[line])
        while j < numberOfValues:
            column = random.randint(0, p - 1)
            while len(values[column]) >= 10:
                column = random.randint(0, p - 1)

            value = random.randint(0, 30)
            values[line].append((value, column))
            values[column].append((value, line))
            j += 1

    val_col = []
    for line in range(0, p):
        val_col.append((0, - line))
        for item in values[line]:
            val_col.append(item)
    val_col.append((0, -p))
    print(len(diag))
    print(val_col)

    return SparseMatrix(n, diag, val_col, "generateedMatrix")


def valori_proprii(A):
    x = np.random.randint(100, size=A.n)
    v = np.divide(x, np.linalg.norm(x))
    w = multiply_vector(A, v)

    v = np.divide(w, np.linalg.norm(w))
    w = multiply_vector(A, v)
    l = sum(w[i] * v[i] for i in range(0, A.n))
    k = 1
    while np.linalg.norm(np.subtract(w, np.multiply(l, v))) > A.n * 1e-10 and k <= k_max:
        print("K:", k)
        v = np.divide(w, np.linalg.norm(w))
        w = multiply_vector(A, v)
        l = sum(w[i] * v[i] for i in range(0, A.n))
        k += 1
    return v


def getSingularValuesAndRang(S):
    singularValues = []
    matrixRang = 0
    for i in range(0, len(S)):
        if S[i] >= 0:
            if S[i] > 0:
                matrixRang += 1
            singularValues.append(S[i])

    return singularValues, matrixRang


def getCondionNumber(S):
    o_max = S[0]
    o_min = S[len(S) - 1]
    index = len(S) - 2
    while o_min < 0:
        o_min = S[index]
        index -= 1
    return o_max / o_min


def getAsMatrix(U, S, V, nr_iteratii, p, n):
    # o_i * u_i * v_i_t
    A_s = np.zeros((p, n))
    # for i in range(0, nr_iteratii):
    #     print("Iteratia", i)
    #     aux = np.zeros((p, n))
    #     for j in range(0, p):
    #         for k in range(0, n):
    #             aux[j, k] = U[j][i] * V[i][k]
    #     A_s = np.add(A_s, aux * S[i])
    for i in range(0, nr_iteratii):
        # print("Iteratia:", i)
        u_i = np.array([U[j][i] for j in range(0, p)])
        result = np.multiply.outer(u_i, V[i])
        A_s = np.add(A_s, S[i] * result)
    return A_s
