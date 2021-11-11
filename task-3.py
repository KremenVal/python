class Cell:
    def __init__(self, amount: int):
        self.number_cells = amount

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        new_cell = self.number_cells - other.number_cells

        if new_cell < 0:
            raise ValueError('Вы не можете получить клетку с отрицательным количеством ячеек.')

        return Cell(new_cell)

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __truediv__(self, other):
        return Cell(self.number_cells // other.number_cells)

    def make_order(self, cell, number_cells):
        if not isinstance(cell, Cell):
            raise ValueError('Переданный аргумент не является экземпляром класса Cell.')

        result = ''.join([('*' * number_cells) + '\n' for _ in range(cell.number_cells // number_cells)])
        return result + '*' * (cell.number_cells % number_cells)


cell_1 = Cell(12)
cell_2 = Cell(15)
cell_add = cell_1 + cell_2
cell_sub = cell_2 - cell_1
cell_mul = cell_1 * cell_2
cell_div = cell_1 / cell_2
# cell_sub_negative = cell_1 - cell_2
print(cell_1.number_cells)
print(cell_2.number_cells)
print(cell_add.number_cells)
print(cell_sub.number_cells)
# print(cell_sub_negative.number_cells)
print(cell_mul.number_cells)
print(cell_div.number_cells)
print(cell_1.make_order(cell_2, 5))
