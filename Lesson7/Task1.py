class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_tmp = ''
        for row in self.matrix:
            for elem in row:
                str_tmp += ' ' if len(str(elem)) > 1 else '  ' # чтобы более-менее ровно рисовалась матрица :)
                str_tmp += str(elem) + ' '
            str_tmp += '\n'
        return  str_tmp

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix): # если ранги матриц не равны возвращаем None
            return None
        res = self.matrix # просто инициализация переменной
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)

m1 = Matrix([[31, 32], [37, 43], [51, 86]])
m2 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
m3 = Matrix([[1, 2], [7, 4], [5, 6]])

print(m1)
print(m2)
print(m3)
print('Сложение матриц')
print(m1 + m3)
