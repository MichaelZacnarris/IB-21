class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # магический метод __eq__ - сравнение Позволяет реализовать проверку на равенство для
        # экземпляров пользовательских типов (другие __ne__(), __lt__(), __le__(), __gt__() и __ge__())
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")

p1 = Point(0, 0)
p2 = Point(0, 0)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")

p1 = Point(0, 10)
p2 = Point(0, 0)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")