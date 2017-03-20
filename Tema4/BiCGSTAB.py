epsilon = 1e-16


def solve_system_bicgstab(A, b):
    """Initial guess in zero-vector"""
    x = [0.0] * A.n

    "Initial residual is vector b"

    r0 = [b[i] for i in range(A.n)]
    r = list(r0)
    rho = alpha = omega = 1.0
    v = p = [0.0] * A.n
    k = 0
    for k in range(0, 10 ** 8):
        rho_next = sum(r0[i] * r[i] for i in range(0, A.n))
        beta = (rho_next / rho) * (alpha / omega)
        rho = rho_next

        p = [p[i] - omega * v[i] for i in range(0, A.n)]
        p = [p[i] * beta for i in range(0, A.n)]
        p = [p[i] + r[i] for i in range(0, A.n)]

        v = multiply_vector(A, p)
        alpha = rho_next / sum(r0[i] * v[i] for i in range(0, A.n))
        h = []
        for i in range(0, A.n):
            h.append(x[i] + alpha * p[i])

        found = True
        for i in range(0, A.n):
            aux = abs(h[i] - x[i])
            if aux >= epsilon and found:
                found = False

        if found:
            x = h
            break

        s = [r[i] - alpha * v[i] for i in range(0, A.n)]
        t = multiply_vector(A, s)
        omega = sum(t[i] * s[i] for i in range(A.n)) / sum(t[i] ** 2 for i in range(0, A.n))

        x_next = [h[i] + omega * s[i] for i in range(0, A.n)]
        found = True
        for i in range(0, A.n):
            aux = abs(x_next[i] - x[i])
            if aux >= epsilon and found:
                found = False

        if found:
            x = x_next
            break

        x = x_next
        r = [s[i] - omega * t[i] for i in range(0, A.n)]
        print(k)

    if found == False:
        print("Divergenta")
        return "Divergenta"
    else:
        aux = multiply_vector(A, x)
        error = max([aux[i] - b[i] for i in range(0, A.n)])
        print("X:{x}".format(x=x))
        print("Error:{error}".format(error=error))
        return x[:5], k


def multiply_vector(A, x):
    vector_sol = [0.0] * A.n
    startIndex = 0
    length = len(A.val_col)
    while startIndex < length - 1:
        line = -A.val_col[startIndex][1]
        vector_sol[line] += A.d[line] * x[line]  # adaugam diagonala
        startIndex += 1
        endIndex = startIndex
        while A.val_col[endIndex][1] >= 0:
            column = A.val_col[endIndex][1]
            value = A.val_col[endIndex][0]
            vector_sol[line] += value * x[column]
            endIndex += 1
        startIndex = endIndex

    return vector_sol