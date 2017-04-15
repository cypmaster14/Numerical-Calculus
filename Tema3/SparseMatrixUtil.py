def transform(n, elements, matrix_name):
    nn_count = [0] * 100  # not null count , un vector de frecventa ce contorizeaza numarul de nn de le fiecare linie
    d = [0] * n
    hash_map = dict()
    for element in elements:
        v = element[0]
        i = element[1]
        j = element[2]
        if i == j:
            d[i] = v
        else:
            line_elements = hash_map.get(i)
            if line_elements != None:
                found = False
                for line_element in line_elements:
                    if line_element[1] == j:
                        line_element[0] += v
                        found = True
                        break
                if not found:
                    line_elements.append([v, j])
            else:
                new_line = list()
                new_line.append([v, j])
                hash_map[i] = new_line
    val_col = []
    for line in range(0, n + 1):
        val_col.append((0, -line))
        line_elements = hash_map.get(line)
        if line_elements != None:
            for (val, col) in line_elements:
                val_col.append((val, col))
    return (d, val_col)


def matrixes_are_equal(A, B):
    if A.n != B.n:
        return False
    if len(A.val_col) != len(B.val_col) or len(A.d) != len(B.d):
        return False
    for i in range(0, A.n):
        if A.d[i] != B.d[i]:
            return False
    A_sorted = sorted(A.val_col, key=lambda tup: (tup[0], tup[1]))
    B_sorted = sorted(B.val_col, key=lambda tup: (tup[0], tup[1]))
    epsilon = 0
    for i in range(0, len(A_sorted)):
        if abs(A_sorted[i][0] - B_sorted[i][0]) > epsilon or A_sorted[i][1] != B_sorted[i][1]:
            return False
    return True


def vectors_are_equal(v, b):
    if len(v) != len(b):
        return False
    for i in range(0, len(v)):
        if v[i] != b[i]:
            return False
    return True
