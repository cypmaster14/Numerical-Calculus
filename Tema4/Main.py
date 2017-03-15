from Tema3.Main import read_values
from Tema3.SparseMatrixUtil import transform
from Tema3.SparseMatrix import SparseMatrix
import numpy
from tkinter import *

epsilon = 1e-16
k_max = 10000

root = Tk()
lb2 = Label(root)
lb3 = Label(root)
lb5 = Label(root)
lb6 = Label(root)
lb8 = Label(root)
lb9 = Label(root)
lb11 = Label(root)
lb12 = Label(root)


def read_matrix(filename):
    matrix_name = filename.split(".")[0].upper()
    matrix_data = read_values(filename)
    n = matrix_data[0]
    b = matrix_data[1]
    matrix_d, matrix_val_col = transform(n, matrix_data[2], matrix_name)
    A = SparseMatrix(n, matrix_d, matrix_val_col, matrix_name)
    return A, b


def checkD(d):
    for i in range(0, len(d)):
        if abs(d[i]) <= epsilon:
            return False
    return True


def Gauss_Seidel(A, b):
    if checkD(A.d) == False:
        print("D contains at least a null element")
        exit()

    x_c = [0] * A.n
    x_p = [i for i in range(1, A.n + 1)]
    compute_X_c(A, b, x_c, x_p)
    vector_difference = [x_c[i] - x_p[i] for i in range(0, len(x_c))]
    norm = numpy.linalg.norm(vector_difference, ord=numpy.inf)  # ||X|| infinite= max(|X1|,|X2|,....|Xn|)

    if norm < epsilon or norm > 10 ** 8:
        return x_c, norm, 1

    k = 1
    while norm >= epsilon and k < k_max and norm <= 10 ** 8:
        x_p = list(x_c)
        compute_X_c(A, b, x_c, x_p)
        vector_difference = [x_c[i] - x_p[i] for i in range(0, len(x_c))]
        norm = numpy.linalg.norm(vector_difference, ord=numpy.inf)
        k += 1

    return x_c, norm, k


def compute_X_c(A, b, x_c, x_p):
    startIndex = 0
    while startIndex < len(A.val_col) - 1:
        line = -A.val_col[startIndex][1]
        x_c[line] = b[line]
        startIndex += 1
        endIndex = startIndex
        while A.val_col[endIndex][1] >= 0:
            column = A.val_col[endIndex][1]
            if column < line:
                x_c[line] -= A.val_col[endIndex][0] * x_c[column]
            else:
                x_c[line] -= A.val_col[endIndex][0] * x_p[column]
            endIndex += 1
        x_c[line] /= A.d[line]
        startIndex = endIndex


def initUI(parent):
    parent.title("Tema4")
    global lb2, lb3, lb5, lb6, lb8, lb9, lb11, lb12

    frame1 = Frame(parent)
    frame1.pack(fill=X)

    lb1 = Label(frame1, text="Fisier 1", width=9)
    lb1.pack(side=LEFT, padx=5, pady=5)

    lb2 = Label(frame1, text="Iteratii:", width=9)
    lb2.pack(side=LEFT, padx=5, pady=5)

    frame2 = Frame(parent)
    frame2.pack(fill=X)

    lb3 = Label(frame2, text="Solutii", width=200)
    lb3.pack(side=LEFT, padx=5, pady=5)

    frame3 = Frame(parent)
    frame3.pack(fill=X)

    lb4 = Label(frame3, text="Fisier 2", width=9)
    lb4.pack(side=LEFT, padx=5, pady=5)

    lb5 = Label(frame3, text="Iteratii:", width=9)
    lb5.pack(side=LEFT, padx=5, pady=5)

    frame4 = Frame(parent)
    frame4.pack(fill=X)

    lb6 = Label(frame4, text="Solutii", width=200)
    lb6.pack(side=LEFT, padx=5, pady=5)

    frame5 = Frame(parent)
    frame5.pack(fill=X)

    lb7 = Label(frame5, text="Fisier 3", width=9)
    lb7.pack(side=LEFT, padx=5, pady=5)

    lb8 = Label(frame5, text="Iteratii:", width=9)
    lb8.pack(side=LEFT, padx=5, pady=5)

    frame6 = Frame(parent)
    frame6.pack(fill=X)

    lb9 = Label(frame6, text="Solutii", width=200)
    lb9.pack(side=LEFT, padx=5, pady=5)

    frame7 = Frame(parent)
    frame7.pack(fill=X)

    lb10 = Label(frame7, text="Fisier 4", width=9)
    lb10.pack(side=LEFT, padx=5, pady=5)

    lb11 = Label(frame7, text="Iteratii:", width=9)
    lb11.pack(side=LEFT, padx=5, pady=5)

    frame8 = Frame(parent)
    frame8.pack(fill=X)

    lb12 = Label(frame8, text="Solutii", width=500)
    lb12.pack(side=LEFT, padx=5, pady=5)

    frame9 = Frame(parent)
    frame9.pack(fill=X)

    button1 = Button(frame9, text="Calculate GS", command=main, width=10)
    button1.pack(side=LEFT, padx=50, pady=30)


def main():
    for i in range(1, 5):
        A, b = read_matrix("m_rar_2017_{i}.txt".format(i=i))
        print(A.d[:10], "\n", A.val_col[:10])
        x_c, norm, k = Gauss_Seidel(A, b)
        if norm >= epsilon:
            print("Divergenta\n")

        print("X:", x_c)
        print("Norma:", norm)
        print("Numar de iteratii:", k)
        print("\n\n")

        if i == 1:
            aux = list(map(lambda x: "%.5f" % x, x_c[:5]))
            lb2['text'] = "Iteratii:" + str(k)
            lb3['text'] = aux
        elif i == 2:
            aux = list(map(lambda x: "%.5f" % x, x_c[:5]))
            lb5['text'] = "Iteratii:" + str(k)
            lb6['text'] = aux
        elif i == 3:
            aux = list(map(lambda x: "%.5f" % x, x_c[:5]))
            lb8['text'] = "Iteratii:" + str(k)
            lb9['text'] = aux
        elif i == 4:
            aux = list(map(lambda x: "%.5f" % x, x_c[:5]))
            lb11['text'] = "Iteratii:" + str(k)
            lb12['text'] = aux


if __name__ == "__main__":
    root.geometry("700x700+300+300")
    initUI(root)
    root.mainloop()
