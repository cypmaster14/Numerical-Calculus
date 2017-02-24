from Ex1 import compute_u
from random import uniform
from tkinter import *


# (x+y)+z = x+(y+z)  , y=u, z=u
def checkAssociativityForAddition(x: float) -> bool:
    u = compute_u()
    return (x + u) + u == x + (u + u)


# x,u,y we generated random
def checkAssociativityForMultiplication() -> dict:
    u = uniform(0, 1)
    x = uniform(0, 1)
    y = uniform(0, 1)
    while (x * y) * u == x * (y * u):
        x = uniform(0, 1)
        y = uniform(0, 1)
        u = uniform(0, 1)
    print("X={x}\nY={y}\nU={u}".format(x=x, y=y, u=u))

    return \
        {
            'isAssociative': 'False',
            'x': x,
            'y': y,
            'u': u
        }


if __name__ == "__main__":
    root = Tk()
    root.geometry("230x300")
    root.title('Exercitiul 2')
    app = Frame(root)
    app.pack()

    Label(app, text='Adunarea este asociativa:{aux}'.format(aux=checkAssociativityForAddition(1.0))).grid()
    aux = checkAssociativityForMultiplication()
    Label(app,
          text='Inmultirea este asocitiva:{aux}\n\nx={x}\ny={y}\nu={u}'.format(aux=aux['isAssociative'], x=aux['x'],
                                                                               y=aux['y'],
                                                                               u=aux['u'])).grid()
    print('Addition is associative:', checkAssociativityForAddition(1.0))
    print('Multiplication is associative:', checkAssociativityForMultiplication()['isAssociative'])

    root.mainloop()
