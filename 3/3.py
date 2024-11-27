import math

# Родительский класс
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Метод должен быть переопределен в подклассе.")

# Подкласс для прямоугольника
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Подкласс для круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

# Подкласс для треугольника
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Тестирование
if __name__ == "__main__":
    # Создаем объект прямоугольника
    rectangle = Rectangle(6, 4)
    print(f"Площадь прямоугольника: {rectangle.calculate_area()}")

    # Создаем объект круга
    circle = Circle(5)
    print(f"Площадь круга: {circle.calculate_area():.2f}")

    # Создаем объект треугольника
    triangle = Triangle(10, 8)
    print(f"Площадь треугольника: {triangle.calculate_area()}")