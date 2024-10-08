class Figure:
    __sides = []
    __color = ()
    sides_count = 0
    filled = True

    def __init__(self, color: tuple, *sides):
        self.__color = self.__is_valid_color(color)
        self.__sides = self.__is_valid_sides(sides)

    def __len__(self):
        len_ = 0
        for i in self.get_sides():
            len_ += i
        return len_

    def __is_valid_color(self, color: tuple):
        if len(color) == 3:
            for i in color:
                if i <= 0 or i >= 255:
                    return False
            return color

    def set_color(self, *rgb):
        if (self.__is_valid_color(rgb)):
            self.__color = rgb

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            array_ = []
            for i in sides:
                array_.append(i)
            return array_
        elif len(sides) == 1:
            return [sides[0]] * self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            sides_input = []
            for i in new_sides:
                sides_input.append(i)
            self.__sides = sides_input

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1


class Triangle(Figure):
    sides_count = 3


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
