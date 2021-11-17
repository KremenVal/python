class Complex:
    def __init__(self, a: int, b: int):
        self.complex = complex(a, b)

    def __add__(self, other):
        return Complex(self.complex + other.complex, 0)

    def __mul__(self, other):
        return Complex(self.complex * other.complex, 0)


complex_1 = Complex(2, 3)
complex_2 = Complex(4, 5)
complex_3 = complex_1 + complex_2
complex_4 = complex_1 * complex_2
print(complex_1.complex)
print(complex_2.complex)
print(complex_3.complex)
print(complex_4.complex)
