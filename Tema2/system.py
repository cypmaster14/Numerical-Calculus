import json
import numpy
import Tema2.matrixValidation as matrixValidation
import Tema2.choleskyFunctions as choleskyFunctions
import Tema2.systemSolver as systemSolver
import Tema2.norms as norms
from tkinter import *
import tkinter.messagebox


class System(Frame):
    def __init__(self, fileName, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.read_input(fileName)
        numpy.set_printoptions(suppress=True)
        self.initUi()

    def initUi(self):
        self.parent.title("Tema2")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="N:", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        self.entry1 = Entry(frame1)
        self.entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Matrix:", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl4 = Label(frame4, text="B:", width=6)
        lbl4.pack(side=LEFT, padx=5, pady=5)

        self.entry4 = Entry(frame4)
        self.entry4.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=X)

        lbl5 = Label(frame5, text="e:", width=6)
        lbl5.pack(side=LEFT, padx=5, pady=5)

        self.entry5 = Entry(frame5)
        self.entry5.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        button = Button(frame3, text="Calculate", command=self.buttonClicked, width=10);
        button.pack(side=LEFT, padx=5, pady=5)

    def buttonClicked(self):
        print("Button clicked")
        n = int(self.entry1.get())
        A = self.entry2.get()
        b = self.entry4.get()
        b = b[1:-1]
        e = float(self.entry5.get())
        if n == "" or A == "" or b == "" or e == "":
            tkinter.messagebox.showinfo("Eroare", "Completeaza toate campurile")
            return
        print(A, b, e)
        self.A = numpy.matrix(A, dtype=numpy.float_)
        self.d = numpy.zeros(n, dtype=numpy.float_)
        self.b = numpy.fromstring(b, dtype=numpy.float_, count=n, sep=',')
        self.n = n
        self.e = e

        print(self.A, "\n", self.b)
        self.doHomework()

    def read_input(self, fileName):
        data = json.load(open(fileName, mode="rt"))
        self.A = numpy.matrix(data['A'], dtype=numpy.float_)
        self.d = numpy.zeros(data['n'], dtype=numpy.float_)
        self.b = numpy.array(data['b'], dtype=numpy.float_)
        self.n = data['n']
        self.e = data['e']

    def inputIsValid(self):
        return matrixValidation.matrixIsGood(self.A)

    def printMatrixL(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if i < j:
                    print(0, end=" ")
                elif i == j:
                    print(1, end=" ")
                else:
                    print(self.A[i, j], end=" ")
            print()

        text = "L:\n"
        for i in range(0, self.n):
            for j in range(0, self.n):
                if i < j:
                    text += "0 "
                elif i == j:
                    text += "1 "
                else:
                    text += str(self.A[i, j]) + " "
            text += "\n"

        return text

    def revertToAinit(self):
        for i in range(1, self.n):
            for j in range(i + 1, self.n):
                self.A[j, i] = self.A[i, j]

    def doHomework(self):
        if not self.inputIsValid():
            print('Input is not correct')
            exit()

        # root = Tk()
        # root.title('Tema2')
        # root.geometry("300x450")
        # app = Frame(root)
        # app.pack()


        choleskyFunctions.choleskyDecomposition(self.A, self.d, self.e)
        matrixL = self.printMatrixL()
        Label(self.parent, text=matrixL).pack()
        Label(self.parent, text="d={d}".format(d=self.d)).pack()
        Label(self.parent, text=choleskyFunctions.choeleskyDeterminant(self.d))
        print("d=", self.d)
        print("Determinant of A=", choleskyFunctions.choeleskyDeterminant(self.d))
        xChol = systemSolver.solveSystem(self.A, self.d, self.b)
        Label(self.parent, text="xChol:{x}".format(x=xChol)).pack()
        print("xChol:", xChol)

        self.revertToAinit()
        L, U = choleskyFunctions.choleskyLUDecomposition(self.A)
        print("L={l}".format(l=L))
        print("U={u}".format(u=U))
        print("X=", systemSolver.solveSystemClasically(self.A, self.b))
        print("L*U=", numpy.dot(L, U))
        Label(self.parent, text="L=\n{l}".format(l=L)).pack()
        Label(self.parent, text="U=\n{u}".format(u=U)).pack()
        Label(self.parent, text="X={value}".format(value=systemSolver.solveSystemClasically(self.A, self.b))).pack()

        norm = norms.getSecondNorm(self.A, xChol, self.b)
        print('Eucledian norm:{norm}'.format(norm=norm))
        Label(self.parent, text='Eucledian norm:{norm}'.format(norm=norm)).pack()

        # root.mainloop()
