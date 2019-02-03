# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

print('Задание 1',)
print()

class Triangle():
    def __init__(self,A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.AB = self.length(A, B)
        self.AC = self.length(A, C)
        self.BC = self.length(B, C)

    def length(self,A, B):
        return round(math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2), 1)

    def perimeter(self):
        return round(self.AC + self.AB + self.BC, 1)

    def area(self):
        S = (self.AB + self.AC + self.BC) / 2
        area = math.sqrt(S * (S - self.AB) * (S - self.AC)* (S - self.BC))
        return round(area, 1)

    def heights(self):
        return[round(self.area() / base, 1) 
            for base in [self.AB, self.AC, self.BC]]

INFO = Triangle((1,8), (3,5), (9,6))
print('Треугольник:',)
print(' Периметр: ', INFO.perimeter())
print(' Площадь: ', INFO.area())
print(' Высота: ', INFO.heights())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

"""
Вторую задачу не успел. Дошлю
"""
