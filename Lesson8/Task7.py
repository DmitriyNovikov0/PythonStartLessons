class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        tmp_str = f'+ {self.b + other.b}' if (self.b + other.b) > 0 else f'- {-1 * (self.b + other.b)}'
        return f'z = {self.a + other.a} {tmp_str}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        tmp_str = f'+ {self.b * other.a + self.a * other.b}' if (self.b * other.a + self.a * other.b) > 0 else f'- {-1 * (self.b * other.a + self.a * other.b)}'
        return f'z = {self.a * other.a - self.b * other.b} {tmp_str}i'

    def __str__(self):
        tmp_str = f'+ {self.b}' if self.b > 0 else f'- {-1 * (self.b)}'
        return f'{self.a} {tmp_str}i'

z1 = ComplexNumber(2, -5)
z2 = ComplexNumber(1, 4)
print(f'z1 = {z1}')
print(f'z2 = {z2}')
print(z1 + z2)
print(z1 * z2)