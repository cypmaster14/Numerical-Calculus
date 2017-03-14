from SparseMatrix import SparseMatrix
from SparseMatrixUtil import transform
from SparseMatrixUtil import matrixes_are_equal
from SparseMatrixUtil import vectors_are_equal
from tkinter import *

root = Tk()
lb2 = Label(root)
lb4 = Label(root)
lb6 = Label(root)
lb8 = Label(root)
lb10 = Label(root)
lb12 = Label(root)


def read_values(filename):
    with open(filename) as f:
        n = int(f.readline())
        b = list()
        f.readline()
        for i in range(0, n):
            v = f.readline()
            b.append(float(v))
        f.readline()
        matrix = f.read()
        lines = matrix.split("\n")
        del lines[-1]
        data = []
        for line in lines:
            values = line.split(',')
            data.append((float(values[0]), int(values[1]), int(values[2])))
        return (n, b, data)


def read_matrix(filename):
    matrix_name = filename.split(".")[0].upper()
    matrix_data = read_values(filename)
    n = matrix_data[0]
    b = matrix_data[1]
    matrix_d, matrix_val_col = transform(n, matrix_data[2], matrix_name)
    M = SparseMatrix(n, matrix_d, matrix_val_col, matrix_name)
    print(matrix_name + " diagonals (first 10) = " + str(M.d[0:10]))
    print(matrix_name + " val_col (first 10) = " + str(M.val_col[0:10]))
    M_timesX = M.multiply_vector()
    vectors_equal = str(vectors_are_equal(M_timesX, b))
    if matrix_name == 'A':
        lb6['text'] = vectors_equal
    else:
        lb8['text'] = vectors_equal
    print(matrix_name + " * x == b? : " + vectors_equal + "\n")
    return M


def check_a_plus_b(A, B):
    a_plus_b_data = read_values("aplusb.txt")
    n = a_plus_b_data[0]
    b = a_plus_b_data[1]
    aplusb_d, aplusb_val_col = transform(n, a_plus_b_data[2], "AplusB")
    AplusB_file = SparseMatrix(n, aplusb_d, aplusb_val_col, "AplusB_file")
    AplusB = A.add_matrix(B)
    AplusB_timesX = AplusB.multiply_vector()
    matrix_equal = str(matrixes_are_equal(AplusB, AplusB_file))
    vector_equal = str(vectors_are_equal(AplusB_timesX, b))
    lb2['text'] = matrix_equal
    lb12['text'] = vector_equal
    print("A plus B == A plus B from file? : " + matrix_equal)
    print("(A+B) * x == b? : " + vector_equal + "\n")


def check_a_x_b(A, B):
    a_x_b_data = read_values("aorib.txt")
    n = a_x_b_data[0]
    b = a_x_b_data[1]
    axb_d, axb_val_col = transform(n, a_x_b_data[2], "AxB")
    AxB_file = SparseMatrix(n, axb_d, axb_val_col, "AxB_file")
    AxB = A.multiply_matrix_super_efficient(B)
    AxB_timesX = AxB.multiply_vector()
    matrix_equal = str(matrixes_are_equal(AxB, AxB_file))
    vectors_equal = str(vectors_are_equal(AxB_timesX, b))
    lb4['text'] = matrix_equal
    lb10['text'] = vectors_equal
    print("A x B == A x B from file? " + matrix_equal)
    print("(AxB) * x == b? : " + vectors_equal)


def main():
    A = read_matrix("a.txt")
    B = read_matrix("b.txt")
    check_a_plus_b(A, B)
    check_a_x_b(A, B)


def initUI(parent):
    parent.title("Tema3")
    global lb2, lb4, lb6, lb8, lb10, lb12

    frame1 = Frame(parent)
    frame1.pack(fill=X)

    lb1 = Label(frame1, text="A + B == A + B from file?", width=24)
    lb1.pack(side=LEFT, padx=5, pady=5)

    lb2 = Label(frame1, text="True or False", width=14)
    lb2.pack(side=LEFT, padx=5, pady=5)

    frame7 = Frame(parent)
    frame7.pack(fill=X)

    lb11 = Label(frame7, text="(A + B) * x == b?", width=24)
    lb11.pack(side=LEFT, padx=5, pady=5)

    lb12 = Label(frame7, text="True or False", width=14)
    lb12.pack(side=LEFT, padx=5, pady=5)

    frame2 = Frame(parent)
    frame2.pack(fill=X)

    lb3 = Label(frame2, text="A x B == A x B from file?", width=24)
    lb3.pack(side=LEFT, padx=5, pady=5)

    lb4 = Label(frame2, text="True or False", width=14)
    lb4.pack(side=LEFT, padx=5, pady=5)

    frame6 = Frame(parent)
    frame6.pack(fill=X)

    lb9 = Label(frame6, text="(A x B) * x == b?", width=24)
    lb9.pack(side=LEFT, padx=5, pady=5)

    lb10 = Label(frame6, text="True or False", width=14)
    lb10.pack(side=LEFT, padx=5, pady=5)

    frame3 = Frame(parent)
    frame3.pack(fill=X)

    lb5 = Label(frame3, text="A * x == b?", width=24)
    lb5.pack(side=LEFT, padx=5, pady=5)

    lb6 = Label(frame3, text="True or False", width=14)
    lb6.pack(side=LEFT, padx=5, pady=5)

    frame5 = Frame(parent)
    frame5.pack(fill=X)

    lb7 = Label(frame5, text="B * x == b?", width=24)
    lb7.pack(side=LEFT, padx=5, pady=5)

    lb8 = Label(frame5, text="True or False", width=14)
    lb8.pack(side=LEFT, padx=5, pady=5)

    frame4 = Frame(parent)
    frame4.pack(fill=X)

    button1 = Button(frame4, text="Calculate", command=main, width=10)
    button1.pack(side=LEFT, padx=50, pady=30)


if __name__ == "__main__":
    root.geometry("700x700+300+300")
    initUI(root)
    root.mainloop()
