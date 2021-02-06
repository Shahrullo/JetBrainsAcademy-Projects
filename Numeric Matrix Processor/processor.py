import math
from operator import add

class Matrix:
    def __init__(self):
        self.mess = None

    # reading matrices
    def initial_matrix(self):
        a, b = input('Enter size of first matrix: ').split()
        m1 = []
        print('Enter first matrix:')
        for _ in range(int(a)):
            m1.append([int(x) if x.isdigit() else float(x) for x in input().split()])

        c, d = input('Enter size of second matrix: ').split()
        m2 = []
        print('Enter second matrix:')
        for _ in range(int(c)):
            m2.append([int(x) if x.isdigit() else float(x) for x in input().split()])
        return m1, m2

    # adding matrix
    def matrix_addition(self):
        addition = []
        m1, m2 = self.initial_matrix()
        a = len(m1)
        b = len(m1[0])
        c = len(m2)
        d = len(m2[0])
        if a == c and b == d:
            for j in range(len(m1)):
                addition.append(list(map(add, m1[j], m2[j])))
            print('The result is:')
        else:
            print('The operation cannot be performed.')

        for i in addition:
            line = []
            for el in i:
                line.append(str(el))
            line = ' '.join(line)
            print(line)

    # scalar matrix multiplication
    def scalar_matrix(self):
        a, b = input('Enter size of matrix: ').split()
        matrix = []
        multiplied = []
        print('Enter matrix:')
        for _ in range(int(a)):
            matrix.append([int(x) if x.isdigit() else float(x) for x in input().split()])
        scala = float(input('Enter constant: '))
        print('The result is:')
        for i in matrix:
            line = list(map(lambda x: x * scala, i))
            print(*line, sep=' ')

    # multiplication of matrices
    def matrix_multiply(self):
        m1, m2 = self.initial_matrix()
        b = len(m1[0])
        c = len(m2)
        if b == c:
            result = [[sum(x * y for x, y in zip(row_m1, col_m2))
                       for col_m2 in zip(*m2)] for row_m1 in m1]
            print('The result is:')
            for i in result:
                print(*i, sep=' ')
        else:
            print('The operation cannot be performed.')

    # transpose of matrices
    def matrix_transpose(self):
        types = input("\n1. Main diagonal\n2. Side diagonal\n\
                        3. Vertical line\n4. Horizontal line\nYour choice: ")
        a, b = input('Enter matrix size: ').split()
        matrix = []
        print('Enter matrix:')
        for _ in range(int(a)):
            matrix.append([(x) for x in input().split()])
        if types == '1':
            print('The result is: ')
            main_ = [[matrix[i][j] for i in range(int(a))] for j in range(int(b))]
            for line in main_:
                print(*line, sep=' ')
        elif types == '2':
            print('The result is: ')
            main_ = [[matrix[i][j] for i in range(int(a))] for j in range(int(b))]
            side_ = [main_[-i][::-1] for i in range(1, len(main_) + 1)]
            for line in side_:
                print(*line, sep=' ')
        elif types == '3':
            print('The result is: ')
            vertical_ = [matrix[i][::-1] for i in range(int(a))]
            for line in vertical_:
                print(*line, sep=' ')
        elif types == '4':
            print('The result is:')
            horizontal_ = [matrix[-i] for i in range(1, int(a) + 1)]
            for line in horizontal_:
                print(*line, sep=' ')


    # Determinant of matrices
    def matrix_det(self):
        a, b = input('Enter matrix size: ').split()
        matrix = []
        print('Enter matrix:')
        for _ in range(int(a)):
            matrix.append([int(x) if x.isdigit() else float(x) for x in input().split()])
        # to find minor
        def minor(mat, i, j):
            return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]
        # get determinant of matrices
        def det(mat):
            if len(mat) == 2:
                return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
            elif len(mat) == 1:
                return mat[0][0]

            determinant = 0
            for i in range(len(mat)):
                determinant += ((-1) ** i) * mat[0][i] * det(minor(mat, 0, i))
            return determinant

        result = det(matrix)
        print(f'The result is:\n{result}')

    # Inverse of matrices
    def matrix_inverse(self):
        a, b = input('Enter matrix size: ').split()
        matrix = []
        print('Enter matrix:')
        for _ in range(int(a)):
            matrix.append([int(x) if x.isdigit() else float(x) for x in input().split()])
        # to get minor
        def minor(mat, i, j):
            return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]

        # to get determinant
        def det(mat):
            if len(mat) == 2:
                return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
            elif len(mat) == 1:
                return mat[0][0]

            determinant = 0
            for i in range(len(mat)):
                determinant += ((-1) ** i) * mat[0][i] * det(minor(mat, 0, i))
            return determinant

        # to transpose
        def transposed(mat):
            return list(map(list, zip(*mat)))

        # to inverse
        def mat_inversed(mat):
            determinant = det(mat)
            if determinant == 0:
                return ""
            elif len(mat) == 1:
                return round((1 / mat[0][0]), 3)
            elif len(mat) == 2:
                return [[round((mat[1][1] / determinant), 2), round((-1 * mat[0][1] / determinant), 2)],
                        [round((-1 * mat[1][0] / determinant), 2), round((mat[0][0] / determinant), 2)]]

            cofactor = []

            for i in range(len(mat)):
                c_fac_row = []

                for j in range(len(mat)):
                    n_minor = minor(mat, i, j)
                    c_fac_row.append(((-1) ** (i + j)) * det(n_minor))
                cofactor.append(c_fac_row)
            cofactor = transposed(cofactor)
            for i in range(len(cofactor)):
                for j in range(len(cofactor)):
                    cofactor[i][j] = math.trunc((cofactor[i][j] / determinant) * 100) / 100
            return cofactor

        inverse = mat_inversed(matrix)
        determinant = det(matrix)
        if determinant == 0:
            print('The matrix doesn\'t have an inverse.')
        else:
            print('The result is:')
            print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in inverse]))


    def main(self):
        while True:
            self.mess = input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit\nYour choice: """)
            if self.mess == '1':
                self.matrix_addition()
                print()
            elif self.mess == '2':
                self.scalar_matrix()
                print()
            elif self.mess == '3':
                self.matrix_multiply()
                print()
            elif self.mess == '4':
                self.matrix_transpose()
                print()
            elif self.mess == '5':
                self.matrix_det()
                print()
            elif self.mess == '6':
                self.matrix_inverse()
                print()
            else:
                if self.mess == '0':
                    break


matrix = Matrix()
Matrix.main(matrix)
