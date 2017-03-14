from time import time


class SparseMatrix:
    def __init__(self, n, d, val_col, name):
        self.n = n
        self.d = d
        self.val_col = val_col
        self.name = name

    # 1) Add all the elements from current line of A in AplusB
    # 2) Add the values from B with the values of AplusB if they have the same column
    # 3) If they don't have the same column, add the values as new elements to AplusB
    def add_matrix(self, B):
        AplusB_d = []
        for i in range(0, self.n):
            AplusB_d.append(self.d[i] + B.d[i])
        AplusB_val_col = []
        A_line_index = B_line_index = 0
        A_length = len(self.val_col)
        B_length = len(B.val_col)
        while A_line_index < A_length:
            current_line = -self.val_col[A_line_index][1]
            AplusB_val_col.append([0, -current_line])
            AplusB_line_index = len(AplusB_val_col)

            # Add the elements from the current line of A
            A_line_start = A_line_index + 1
            k = A_line_start
            while k < A_length and self.val_col[k][0] != 0:
                k += 1
            A_line_end = k
            for i in range(A_line_start, A_line_end):
                A_line_element = self.val_col[i]
                AplusB_val_col.append([A_line_element[0], A_line_element[1]])

            # Add the values of elements from the current line of B to the existing values of AplusB if the columns match
            # Else add the (value,column) pairs from B as new elements to AplusB
            B_line_start = B_line_index + 1
            k = B_line_start
            while k < B_length and B.val_col[k][0] != 0:
                k += 1
            B_line_end = k
            for i in range(B_line_start, B_line_end):
                B_element = B.val_col[i]
                found = False
                AplusB_length = len(AplusB_val_col)
                for j in range(AplusB_line_index, AplusB_length):
                    AplusB_element = AplusB_val_col[j]
                    if B_element[1] == AplusB_element[1]:
                        AplusB_element[0] += B_element[0]
                        found = True
                        break
                if not found:
                    AplusB_val_col.append([B_element[0], B_element[1]])
            A_line_index = A_line_end
            B_line_index = B_line_end
        print("AplusB diagonals (first 10) = " + str(AplusB_d[0:10]))
        print("AplusB val_col (first 10) = " + str(AplusB_val_col[0:10]))
        AplusB = SparseMatrix(self.n, AplusB_d, AplusB_val_col, "AplusB")
        return AplusB

    # Multiply the matrix with the vector x = (n,n-1,n-2....1)
    def multiply_vector(self):
        vector_sol = []
        line_index = 0
        length = len(self.val_col)
        while line_index < length - 1:
            line = -self.val_col[line_index][1]
            line_sum = self.d[line] * (self.n - line)
            line_start = line_index + 1
            k = line_start
            while k < length and self.val_col[k][0] != 0:
                k += 1
            line_end = k
            for i in range(line_start, line_end):
                element = self.val_col[i]
                line_sum += element[0] * (self.n - element[1])
            vector_sol.append(line_sum)
            line_index = line_end
        print(self.name + " * x (first 10) = " + str(vector_sol[0:10]))
        return vector_sol

    # Multiply each line from A only with valid columns from B (columns of elements on line = A_line_element.column)
    # Compute the sum for each element in AxB by storing and updating the value in a dictionary with key = column -> O(1) access
    # Time coplexity: O(2017 lines x 10 elements per line in A x 10 elements per line in B x 1 for access/update AxB line) -> O(2*10^5)
    def multiply_matrix_super_efficient(self, B):
        t0 = time()
        multiply_val_col = []
        multiply_d = []
        vc_length = len(self.val_col)
        line_index = 0
        B_lines = self.compute_lines_dictionary(B.d, B.val_col)
        while line_index < vc_length - 1:
            line = -self.val_col[line_index][1]
            multiply_val_col.append((0, -line))
            A_line = [(self.d[line], line)]
            k = line_index + 1
            while k < vc_length and self.val_col[k][0] != 0:
                A_line.append(self.val_col[k])
                k += 1

            AxB_line = dict()  # key = col
            for A_line_element in A_line:
                B_line = B_lines[A_line_element[1]]
                for B_line_element in B_line:
                    AxB_line_element = AxB_line.get(B_line_element[1])
                    if AxB_line_element is not None:
                        AxB_line[B_line_element[1]] = AxB_line_element + A_line_element[0] * B_line_element[0]
                    else:
                        AxB_line[B_line_element[1]] = A_line_element[0] * B_line_element[0]

            for col, value in AxB_line.iteritems():
                if col == line:
                    multiply_d.append(value)
                else:
                    multiply_val_col.append((value, col))

            line_index = k

        multiply_val_col.append((0, -self.n))
        tf = time()
        print("AxB time = " + str((tf - t0) * 1000).split(".")[0] + "ms")
        print("AxB diagonals (first 10) = " + str(multiply_d[0:10]))
        print("AxB val_col (first 10) = " + str(multiply_val_col[0:10]))
        AxB = SparseMatrix(self.n, multiply_d, multiply_val_col, "AxB")
        return AxB

    def compute_lines_dictionary(self, d, val_col):
        lines = dict()
        i = 0
        val_col_length = len(val_col)
        while i < val_col_length - 1:
            current_line = -val_col[i][1]
            line_list = [(d[current_line], current_line)]
            i += 1
            while val_col[i][0] != 0:
                line_list.append(val_col[i])
                i += 1
            lines[current_line] = line_list
        return lines

    ################  Other methods for multiplication  ################

    # O(2017 lines x 10 elements per line x 100 valid columns x 10 elements per line) = O(2017 * 10^4) = O(2*10^7)
    def multiply_matrix_efficient(self, B):
        multiply_val_col = []
        multiply_d = []
        vc_length = len(self.val_col)
        line_index = 0
        B_line_indexes = self.compute_line_indexes(
            B.val_col)  # compute the line indexes before, a little bit more efficient
        # For each line
        #     Compute the set valid_columns by adding all the columns of elements from lines = columns(elements from current line in A)
        #     Exemple:
        #       current line in A : (4,3) (2,1)
        #       B : (0,-1) (3,2) (0, -2) (4,4) (1,4) (0, -3) (5,1)(6,3) (3,2) ...
        #       valid_columns = {} (set)
        #       Element (4,3) -> Go in B at line 3 and add all the columns to the set -> valid_columns = {1,3,2}
        #       Element (2,1) -> Go in B at line 1 and add all the columns to the set -> valid_columns = {1,3,2} U {2} = {1,3,2}
        #     For each col in valid_columns
        #         Multiply
        #             the current line element from A at position (line,c)
        #             with the coresponding col element from B at position (c,col)
        while line_index < vc_length - 1:
            line = -self.val_col[line_index][1]
            # print(line)
            multiply_val_col.append((0, -line))
            line_start = line_index + 1
            k = line_start
            while k < vc_length and self.val_col[k][0] != 0:
                k += 1
            line_end = k
            valid_columns = set()
            for i in range(line_start, line_end):
                element_column = self.val_col[i][1]
                valid_columns.update(self.get_valid_columns(B.val_col, element_column, B_line_indexes))
            # Fac si pentru line deoarece daca eu sunt pe linia X in A, nu voi avea ca si indici cal in val_col pe X
            valid_columns.update(self.get_valid_columns(B.val_col, line, B_line_indexes))
            for col in valid_columns:
                if col == line:
                    line_x_col_sum = self.d[col] * B.d[col]
                else:
                    line_x_col_sum = self.d[line] * self.column_element(B.val_col, line, col, B_line_indexes)
                for line_element_index in range(line_start, line_end):
                    element = self.val_col[line_element_index]
                    if element[1] == col:
                        line_x_col_sum += element[0] * B.d[col]
                    else:
                        line_x_col_sum += element[0] * self.column_element(B.val_col, element[1], col, B_line_indexes)

                if line_x_col_sum != 0:
                    if line == col:
                        multiply_d.append(line_x_col_sum)
                    else:
                        multiply_val_col.append((line_x_col_sum, col))
            line_index = line_end
        multiply_val_col.append((0, -self.n))
        print("AxB diagonals (first 10) = " + str(multiply_d[0:10]))
        print("AxB val_col (first 10) = " + str(multiply_val_col[0:10]))
        AxB = SparseMatrix(self.n, multiply_d, multiply_val_col, "AxB")
        return AxB

    # O(2017 lines x 10 elements per line x 2017 columns x 10 elements per line) = O(2017^2 * 100) = O(4*10^8)
    def multiply_matrix(self, B):
        multiply_val_col = []
        multiply_d = []
        vc_length = len(self.val_col)
        line_index = 0
        # B_line_indexes = [-1] * self.n #compute the line indexes while doing the multiplication
        B_line_indexes = self.compute_line_indexes(
            B.val_col)  # compute the line indexes before, a little bit more efficient

        # For each line
        #     For each col in (0,n)
        #         Multiply
        #             the current line element from A at position (line,c)
        #             with the coresponding col element from B at position (c,col)
        while line_index < vc_length - 1:
            line = -self.val_col[line_index][1]
            print(line)
            multiply_val_col.append((0, -line))
            line_start = line_index + 1
            k = line_start
            while k < vc_length and self.val_col[k][0] != 0:
                k += 1
            line_end = k
            for col in range(0, self.n):
                if col == line:
                    line_x_col_sum = self.d[col] * B.d[col]
                else:
                    line_x_col_sum = self.d[line] * self.column_element(B.val_col, line, col, B_line_indexes)
                    # line_x_col_sum = self.d[line] * self.column_element_brute(B.val_col,line,col)
                for line_element_index in range(line_start, line_end):
                    element = self.val_col[line_element_index]
                    if element[1] == col:
                        line_x_col_sum += element[0] * B.d[col]
                    else:
                        line_x_col_sum += element[0] * self.column_element(B.val_col, element[1], col, B_line_indexes)
                        # line_x_col_sum += element[0] * self.column_element_brute(B.val_col,element[1],col)

                if line_x_col_sum != 0:
                    if line == col:
                        multiply_d.append(line_x_col_sum)
                    else:
                        multiply_val_col.append((line_x_col_sum, col))
            line_index = line_end
        multiply_val_col.append((0, -self.n))
        print(multiply_d)
        print(multiply_val_col)
        AxB = SparseMatrix(self.n, multiply_d, multiply_val_col, "AxB")
        return AxB

    # efficient way O(NN) -> O(10)

    def column_element(self, val_col, line, col, B_line_indexes):
        line_index = B_line_indexes[line]
        # if line_index == -1: #used if the line indexes are computed during the multiplication for loops
        #   val_col_length = len(val_col)
        #   for i in range(0,val_col_length):
        #       element = val_col[i]
        #       if element[0] == 0 and element[1] == -line:
        #           line_index = i
        #           B_line_indexes[line] = line_index
        j = line_index + 1
        while val_col[j][0] != 0:
            if val_col[j][1] == col:
                return val_col[j][0]
            j += 1
        return 0

    # brute force O(n) -> O(2017)
    def column_element_brute(self, val_col, line, col):
        val_col_length = len(val_col)
        for i in range(0, val_col_length):
            element = val_col[i]
            if element[0] == 0 and element[1] == -line:
                j = i + 1
                while val_col[j][0] != 0:
                    if val_col[j][1] == col:
                        return val_col[j][0]
                    j += 1
                break
        return 0

    def compute_line_indexes(self, val_col):
        line_indexes = []
        val_col_length = len(val_col)
        for i in range(0, val_col_length):
            element = val_col[i]
            if element[0] == 0:
                line_indexes.append(i)
        return line_indexes

    def get_valid_columns(self, val_col, line, B_line_indexes):
        valid_columns = set()
        valid_columns.add(line)  # the diagonal element
        line_index = B_line_indexes[line]
        j = line_index + 1
        while val_col[j][0] != 0:
            valid_columns.add(val_col[j][1])
            j += 1
        return valid_columns
