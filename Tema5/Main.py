from IterativeInverse import IterativeInverse
import numpy as np

def compute_epsilon():
    m = -1
    u = 10
    while 1.0 + u != 1.0:
        u = 10 ** m
        m -= 1
    return u

def main():
    a = []
    with open("matrix.txt") as f:
        n = int(next(f))
        for line_s in f:  # read rest of lines
            line = [int(x) for x in line_s.split(" ")]
            a.append(line)
    a = np.array(a)
    ii = IterativeInverse(n,compute_epsilon(),1000,a)
    ii.solve(3)

main()