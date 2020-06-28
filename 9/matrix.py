from sys import stdin


def transpose_list_of_lists(list_of_lists):
    return [list(i) for i in zip(*list_of_lists)]


class MatrixError(Exception):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, list_of_lists):
        self._list = [x[:] for x in list_of_lists]

    def internal_list(self):
        return self._list

    def __str__(self):
        return '\n'.join(list(map(lambda row: '\t'.join(map(str, row)),
                         self._list)))

    def __getitem__(self, idx):
        return self._list[idx]

    def size(self):
        return (len(self._list), len(self._list[0]))

    def copy(self):
        return Matrix(self._list)

    def __mul__(self, n):
        new_matrix = self.copy()

        rows, columns = self.size()

        for i in range(rows):
            for j in range(columns):
                new_matrix[i][j] *= n

        return new_matrix

    __rmul__ = __mul__

    def __add__(self, other):
        other = Matrix(other)

        rows, columns = self.size()
        other_rows, other_columns = other.size()

        if rows != other_rows or columns != other_columns:
            raise MatrixError(self, other)

        numbers = []
        result = []
        for i in range(rows):
            for j in range(columns):
                s = other[i][j] + self._list[i][j]
                numbers.append(s)
                if len(numbers) == columns:
                    result.append(numbers)
                    numbers = []

        return Matrix(result)

    def transpose(self):
        tmatrix = list(map(list, zip(*self._list)))
        self._list = tmatrix
        return Matrix(tmatrix)

    @staticmethod
    def transposed(matrix):
        tmatrix = list(map(list, zip(*matrix.internal_list())))
        return Matrix(tmatrix)


exec(stdin.read())
