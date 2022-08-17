class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.simbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if self.cell - other.cell > 0 else 'Ошибка - разнасть меньше 0'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, cell_count, cell_row):
        res = ''
        while cell_count > 0:
            res += '*' * int(cell_row if cell_count > cell_row else cell_count)
            res += '\n'
            cell_count -= cell_row
        return res


a = Cell(5)
b = Cell(10)
print(a + b)
print(a - b)
print(a * b)
print(b / a)
print(a.make_order(a.cell + b.cell, 4))
#получаеться 15 раскидываем по 4 символа в строке, получиться 3 строки по 4 символа и 1 строка 3 символа (3 * 4 + 3 = 15 )