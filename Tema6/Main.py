from Tema6.Utils import *
from tkinter import *
import numpy as np

root = Tk()
entry1 = Entry()
entry2 = Entry()
text = Text()


def button_click():
    p = int(entry1.get())
    n = int(entry2.get())
    text.delete('1.0', END)
    if p == n:
        # if p > 500:
        generatedMatrix, fileMatrix = firstMethod(p, n, "m_rar_sim_2017.txt")
        text.insert(INSERT, "Valori proprii(matrice fisier):{}\n".format(valori_proprii(fileMatrix)[:5]))
        print(valori_proprii(fileMatrix)[:10])
        text.insert(INSERT, "Valori proprii(matrice generata):{}\n".format(valori_proprii(generatedMatrix)[:5]))
        print(valori_proprii(generatedMatrix)[:10])

    if p > n:
        generatedMatrix = np.random.randint(-500, 500, (1, p, n))[0]
        U, s, V = np.linalg.svd(generatedMatrix, full_matrices=True)
        singularValues, matrixRang = getSingularValuesAndRang(s)
        text.insert(INSERT, "Singular Values[{size}]:{values}\nRang:{rang}\n".format(size=len(singularValues),
                                                                                     values=singularValues[:10],
                                                                                     rang=matrixRang))
        # print("Singular Values[{size}]:{values}\nRang:{rang}".format(size=len(singularValues), values=singularValues,
        #                                                              rang=matrixRang))

        text.insert(INSERT, "Condition number:{number}\n".format(number=getCondionNumber(s)))
        # print("Condition number:{number}".format(number=getCondionNumber(s)))
        S = np.zeros((p, n), dtype=complex)
        S[:n, :n] = np.diag(s)
        print(np.allclose(generatedMatrix, np.dot(U, np.dot(S, V))))
        difference = np.subtract(generatedMatrix, np.dot(U, np.dot(S, V)))
        text.insert(INSERT, "Norm:{}\n".format(np.linalg.norm(difference, ord=np.infty)))
        # print("Norm:", np.linalg.norm(difference, ord=np.infty))
        nr_iteratii = random.randint(100, matrixRang)
        text.insert(INSERT, "Numar iteratii:{}\n".format(nr_iteratii))
        # print("Numar iteratii:{}".format(nr_iteratii))
        A_s = getAsMatrix(U, s, V, nr_iteratii, p, n)
        text.insert(INSERT, "A_s:{}\n".format(A_s[0][:10]))
        # print("A_s:{}".format(A_s[0][:10]))
        text.insert(INSERT, "Norm:{}\n".format(np.linalg.norm(np.subtract(generatedMatrix, A_s), ord=np.infty)))
        # print("Norm:{}".format(np.linalg.norm(np.subtract(generatedMatrix, A_s), ord=np.infty)))


def initUI(parent):
    parent.title("Tema 6")
    global entry1, entry2, text

    frame1 = Frame(parent)
    frame1.pack(fill=X)

    lbl1 = Label(frame1, text="P:", width="2")
    lbl1.pack(side=LEFT, padx=5, pady=5)

    entry1 = Entry(frame1, width=10)
    entry1.pack(side=LEFT, padx=5, pady=5)

    lbl1 = Label(frame1, text="N:", width="2")
    lbl1.pack(side=LEFT, padx=5, pady=5)

    entry2 = Entry(frame1, width=10)
    entry2.pack(side=LEFT, padx=5, pady=5)

    button = Button(frame1, text="Calculate", width=10, command=button_click)
    button.pack(padx=5, pady=5)

    frame2 = Frame(parent)
    frame2.pack(fill=X)

    text = Text(frame2, height=200, width=900)
    text.pack(padx=5, pady=5)


if __name__ == "__main__":
    root.geometry("900x700+300+300")
    initUI(root)
    root.mainloop()

    # p = 501
    # n = 501
