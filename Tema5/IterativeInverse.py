import numpy as np


class IterativeInverse:
    def __init__(self, n, epsilon, kmax, A):
        self.n = n
        self.epsilon = epsilon
        self.kmax = kmax
        self.A = A
        self.B = self.get_minus_A()

    def solve(self, method_index):
        if (self.matrix012()):
            print("Inverse:\n " + str(self.method_12()))
            print("Numpy inverse:\n " + str(np.linalg.inv(self.A)))
            return
        V0 = V1 = self.get_init_V()
        k = 0
        delta_V = None
        ten_pow_10 = 10 ** 10
        while (True):
            V0 = V1
            V1 = self.get_next_V(V0, method_index)
            delta_V = self.get_deltaV(V1, V0)
            k += 1
            if (delta_V < self.epsilon or k > self.kmax or delta_V > ten_pow_10):
                break
        print(str(k) + " iterations.")
        if delta_V < self.epsilon:
            norm = self.get_norm(V1)
            iterations = str(k)
            inverse = str(V1)
            numpy_inverse = str(np.linalg.inv(self.A))
            print("Norm:{}\n".format(norm))
            print("Inverse:{}\n ".format(inverse))
            print("Numpy inverse{}:\n ".format(numpy_inverse))
            return norm, iterations, inverse, numpy_inverse

        else:
            print('Divergent')
            return "Divergent"

    def get_minus_A(self):
        zero = np.zeros((self.n, self.n))
        return np.subtract(zero, self.A)

    def get_init_V(self):
        A_transpose = self.A.transpose()
        A1 = np.linalg.norm(self.A, 1)
        Ainf = np.linalg.norm(self.A, np.inf)
        V0 = A_transpose / (A1 * Ainf)
        # V0 = np.divide(A_transpose,np.arange(A1 * Ainf))
        return V0

    def get_next_V(self, V0, method_index):
        if method_index == 1:
            return self.method_1(V0)
        elif method_index == 2:
            return self.method_2(V0)
        else:
            return self.method_3(V0)

    def method_1(self, V0):
        C = np.dot(self.B, V0)
        C = self.add_a_to_diagonal(C, a=2)
        V_next = np.dot(V0, C)
        return V_next

    def method_2(self, V0):
        C = np.dot(self.B, V0)
        V_next = self.add_a_to_diagonal(np.copy(C), a=3)
        V_next = np.dot(C, V_next)
        V_next = self.add_a_to_diagonal(V_next, a=3)
        V_next = np.dot(V0, V_next)
        return V_next

    def method_3(self, V0):
        zero = np.zeros((self.n, self.n))
        minus_vk = np.subtract(zero, V0)
        vka = np.dot(minus_vk, self.A)
        vka3 = self.add_a_to_diagonal(np.copy(vka), a=3)
        vka3 = np.dot(vka3, vka3)
        vka1 = self.add_a_to_diagonal(vka, a=1)
        vka1 = 1.0 / 4.0 * vka1
        vka_dot = np.dot(vka1, vka3)
        vka_dot_plus1 = self.add_a_to_diagonal(vka_dot, a=1)
        V_next = np.dot(vka_dot_plus1, V0)
        return V_next

    def add_a_to_diagonal(self, C, a):
        for i in range(0, self.n):
            C[i][i] += a
        return C

    def get_deltaV(self, V1, V0):
        dif = np.subtract(V1, V0)
        return np.linalg.norm(dif, 1)

    def get_norm(self, A_inv):
        prod = np.dot(self.A, A_inv)
        In = np.identity(self.n)
        diff = np.subtract(prod, In)
        return np.linalg.norm(diff, 1)

    def matrix012(self):
        for i in range(0, self.n):
            if self.A[i][i] != 1:
                return False
            if i < self.n - 1 and self.A[i][i + 1] != 2:
                return False
            for j in range(0, i):
                if self.A[i][j] != 0:
                    return False
            for j in range(i + 2, self.n):
                if self.A[i][j] != 0:
                    return False
        return True

    def method_12(self):
        a = np.zeros((self.n, self.n))
        for i in range(0, self.n):
            a[i][i] = 1
            j = i + 1
            while j < self.n:
                a[i][j] = (-1) ** (j - i) * 2 ** (j - i)
                j += 1
        return a
