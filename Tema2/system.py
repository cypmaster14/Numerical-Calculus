import json
import numpy
import matrixValidation
import choleskyFunctions
import systemSolver
import norms
from tkinter import *


class System(object):
    def __init__(self, fileName):
        self.read_input(fileName)
        numpy.set_printoptions(suppress=True)

    def read_input(self, fileName):
        data = json.load(open(fileName, mode="rt"))
        self.Ainit = numpy.matrix(data['A'])
        self.A = numpy.matrix(data['A'])
        self.d = numpy.zeros(3)
        self.b = numpy.array(data['b'])
        self.n = data['n']

    def inputIsOk(self):
        return matrixValidation.matrixIsGood(self.A, self.n)

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

    def doHomework(self):
        if not self.inputIsOk():
            print('Input is not correct')
            exit()

        root = Tk()
        root.title('Tema2')
        root.geometry("300x450")
        app = Frame(root)
        app.pack()

        choleskyFunctions.choleskyDecomposition(self.A, self.d, self.n)
        matrixL = self.printMatrixL()
        Label(app, text=matrixL).pack()
        Label(app, text="d={d}".format(d=self.d)).pack()
        Label(app, text=choleskyFunctions.choeleskyDeterminant(self.d))
        print("d=", self.d)
        print("Determinant of A=", choleskyFunctions.choeleskyDeterminant(self.d))
        xChol = systemSolver.solveSystem(self.A, self.d, self.n, self.b)
        Label(app, text="xChol:{x}".format(x=xChol)).pack()
        print("xChol:", xChol)

        L, U = choleskyFunctions.choleskyLUDecomposition(self.A)
        print("L={l}".format(l=L))
        print("U={u}".format(u=U))
        print("X=", systemSolver.solveSystemClasically(self.Ainit, self.b))
        Label(app, text="L=\n{l}".format(l=L)).pack()
        Label(app, text="U=\n{u}".format(u=U)).pack()
        Label(app, text="X={value}".format(value=systemSolver.solveSystemClasically(self.Ainit, self.b))).pack()

        norm = norms.getSecondNorm(self.A, xChol, self.b, self.n)
        print('Eucledian norm:{norm}'.format(norm=norm))
        Label(app, text='Eucledian norm:{norm}'.format(norm=norm)).pack()

        root.mainloop()
