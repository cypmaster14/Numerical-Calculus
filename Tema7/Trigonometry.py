import numpy

def get_T(x,n):
    T = []
    for i in range(0,n+1):
        line = []
        for k in range(0,n+1):
            if(k==0):
                line.append(1)
            else:
                if(k%2==1):
                    line.append(numpy.sin((k/2+1)*x[i]))
                else:
                    line.append(numpy.cos((k/2)*x[i]))
        T.append(line)
    return T


def get_X(n, x, Y):
    T = get_T(x, n)
    X = numpy.linalg.solve(numpy.array(T), numpy.array(Y))
    return X


def phi(x,k):
    if(k%2==1):
        return numpy.sin((k/2+1)*x)
    else:
        return numpy.cos((k/2)*x)


def solve(n, x, y, x_new):
    X = get_X(n,x,y)
    sol = 0
    for k in range(0,n):
        sol += X[k] * phi(x_new,k)
    return sol