from tkinter import *
from Tema8.LaguerrePolynomApproximation import get_real_roots
from Tema8.LaguerrePolynomComplexAproximation import get_complex_roots
from Tema8.FunctionMinimize import minimize_function_with_secant
from Tema8.FunctionMinimize import approximate_second_derivatived

root = Tk()
var = StringVar()
entry1 = Entry()
text = Text()


def calculate():
    optionSelected = var.get()
    polynom = [int(coefficient.strip()) for coefficient in
               entry1.get()[1:-1].split(",")]  # get the coefficients of the polynom
    print(polynom)
    text.delete('1.0', END)

    if optionSelected == "1" or optionSelected == "2":
        roots = get_real_roots(polynom) if optionSelected == "1" else get_complex_roots(polynom)
        print("Roots", roots)
        fileObject = open("output.txt", mode="wt")
        fileObject.write("Roots:\n")
        for root in roots:
            text.insert(INSERT, "{}\n".format(root))
            fileObject.write("{}\n".format(root))
        fileObject.close()

    else:
        minim_point = minimize_function_with_secant(polynom, 1) if optionSelected == 3 \
            else minimize_function_with_secant(polynom, 2)
        text.insert(INSERT, "x*={}\n".format(minim_point))
        if minim_point != "Divergenta":
            text.insert(INSERT, "F\'\'(X)>0:{}\n".format(approximate_second_derivatived(polynom, minim_point)))


def initUI(parent):
    parent.title("Tema8")
    global entry1, text
    frame1 = Frame(parent)
    frame1.pack(fill=X)

    lbl1 = Label(frame1, text="Polynom:", width="10")
    lbl1.pack(side=LEFT, padx=5, pady=5)

    entry1 = Entry(frame1, width=50)
    entry1.pack(side=LEFT, padx=5, pady=5)

    R1 = Radiobutton(frame1, text="Real Polynom Solutions", variable=var, value="1")
    R1.pack(padx=5, pady=5)

    R2 = Radiobutton(frame1, text="Complex Polynom Solutions", variable=var, value="2")
    R2.pack(padx=5, pady=5)

    R3 = Radiobutton(frame1, text="Minimize function(i=1)", variable=var, value="3")
    R3.pack(padx=5, pady=5)

    R4 = Radiobutton(frame1, text="Minimize function(i=2)", variable=var, value="4")
    R4.pack(padx=5, pady=5)

    button = Button(frame1, text="Calculate", width=10, command=calculate)
    button.pack(padx=5, pady=5)

    frame2 = Frame(parent)
    frame2.pack(fill=X)

    text = Text(frame2, height=200, width=900)
    text.pack(padx=5, pady=5)


if __name__ == "__main__":
    root.geometry("900x700+300+300")
    initUI(root)
    root.mainloop()
