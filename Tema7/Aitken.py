def get_divided_difference(d0dk,d1k1,x0,xk1):
    return float(d1k1-d0dk) / (xk1-x0)


def get_pair_div_diff(x0, x1, y0, y1):
    return float(y1-y0)/(x1-x0)


def get_initial_div_diff(n, x, f):
    initial_dd = []
    for i in range(0,n):
        initial_dd.append(get_pair_div_diff(x[i], x[i+1], f[i], f[i+1]))
    return initial_dd


def get_divided_differences(n, x, f):
    last = get_initial_div_diff(n,x,f)
    divided_differences = [last[0]]
    for p in range(1,n):
        current = []
        for i in range(0,n-p):
            x0 = x[i]
            xk1 = x[i+p+1]
            #print "x"+str(i) + "=" + str(x0) + " , " + "x"+str(i+p+1) + "=" + str(xk1)
            div_diff = get_divided_difference(last[i],last[i+1],x0,xk1)
            current.append(div_diff)
        last = current
        divided_differences.append(last[0])
    return divided_differences


def diff_product(x_new,x):
    p = x_new-x[0]
    for i in range(1,len(x)):
        p *= (x_new-x[i])
    return p


def Ln(n, x, f, x_new):
    divided_differences = get_divided_differences(n, x, f)
    aprox_f = f[0]
    for i in range(0,n):
        aprox_f += divided_differences[i] * diff_product(x_new,x[0:i+1])

    return aprox_f


# n = 3
# x = [0,1,4,9]
# f = [4,7,2,5]
#
# Ln(n,x,f,10)

