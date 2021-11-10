from abc import abstractmethod


class Clothes:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculating(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        Clothes.__init__(self, name)
        self.size = size
        self.__all_sizes = None

    def calculating(self):
        return round(self.size / 6.5 + 0.5, 2)

    @property
    def all_expense(self):
        if self.__all_sizes is None:
            self.__all_sizes = {i: round(i / 6.5 + 0.5, 2) for i in range(50, 201)}

        return self.__all_sizes


class Suit(Clothes):
    def __init__(self, name, height):
        Clothes.__init__(self, name)
        self.height = height
        self.__all_height = None

    def calculating(self):
        return 2 * self.height + 0.3

    @property
    def all_expense(self):
        if self.__all_height is None:
            self.__all_height = {i: 2 * i + 0.3 for i in range(50, 221)}

        return self.__all_height


my_coat = Coat('Coat', 100)
print(my_coat.calculating())
print(my_coat.all_expense)
my_suit = Suit('Suit', 120)
print(my_suit.calculating())
print(my_suit.all_expense)
