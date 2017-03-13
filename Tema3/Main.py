from SparseMatrix import SparseMatrix
from SparseMatrixUtil import transform
from SparseMatrixUtil import matrixes_are_equal
from SparseMatrixUtil import vectors_are_equal

def read_values(filename):
    with open(filename) as f:
        n = int(f.readline())
        b = list()
        f.readline()
        for i in range(0,n):
            v = f.readline()
            b.append(float(v))
        f.readline()
        matrix = f.read()
        lines = matrix.split("\n")
        del lines[-1]
        data = []
        for line in lines:
            values = line.split(',')
            data.append((float(values[0]),int(values[1]),int(values[2])))
        return (n,b,data)

def read_matrix(filename):
    matrix_name = filename.split(".")[0].upper()
    matrix_data = read_values(filename)
    n = matrix_data[0]
    b = matrix_data[1]
    matrix_d, matrix_val_col = transform(n,matrix_data[2],matrix_name)
    M = SparseMatrix(n,matrix_d,matrix_val_col,matrix_name)
    print matrix_name + " diagonals (first 10) = " + str(M.d[0:10])
    print matrix_name + " val_col (first 10) = " + str(M.val_col[0:10])
    M_timesX = M.multiply_vector()
    print matrix_name + " * x == b? : " + str(vectors_are_equal(M_timesX,b)) + "\n"
    return M

def check_a_plus_b(A,B):
    a_plus_b_data = read_values("aplusb.txt")
    n = a_plus_b_data[0]
    b = a_plus_b_data[1]
    aplusb_d, aplusb_val_col = transform(n,a_plus_b_data[2],"AplusB")
    AplusB_file = SparseMatrix(n,aplusb_d,aplusb_val_col,"AplusB_file")
    AplusB = A.add_matrix(B)
    AplusB_timesX = AplusB.multiply_vector()
    print "A plus B == A plus B from file? : " + str(matrixes_are_equal(AplusB,AplusB_file))
    print "(A+B) * x == b? : " + str(vectors_are_equal(AplusB_timesX,b)) + "\n"

def check_a_x_b(A,B):
    a_x_b_data = read_values("aorib.txt")
    n = a_x_b_data[0]
    b = a_x_b_data[1]
    axb_d, axb_val_col = transform(n,a_x_b_data[2],"AxB")
    AxB_file = SparseMatrix(n,axb_d,axb_val_col,"AxB_file")
    AxB = A.multiply_matrix_efficient(B)
    AxB_timesX = AxB.multiply_vector()
    print "A x B == A x B from file? " + str(matrixes_are_equal(AxB,AxB_file))
    print "(AxB) * x == b? : " + str(vectors_are_equal(AxB_timesX,b))

def main():
    A = read_matrix("a.txt")
    B = read_matrix("b.txt")
    check_a_plus_b(A,B)
    check_a_x_b(A,B)

main()