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

#Доделал вторую задачу:

def side_len(dot1,dot2):
    return math.sqrt((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2)

class Trapezium:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = round(side_len(self.A, self.B), 1)
        self.BC = round(side_len(self.B, self.C), 1)
        self.CD = round(side_len(self.C, self.D), 1)
        self.AD = round(side_len(self.A, self.D), 1)

    def check(self):
        return side_len(self.C, self.A) == side_len(self.B, self.D)


    def perimeter(self):
        return round((self.AD + self.BC + self.CD + self.AD),1)

    def square(self):
        return round(((self.AD + self.BC)/4) * math.sqrt((4 * (self.AB ** 2)) - ((self.AD - self.BC) ** 2)),1)

tr1 = Trapezium((0, 0), (2, 1), (2, 3), (0, 4))
print('Дан четырехугольник, имеющий стороны: {}, {}, {}, {}.'.format(tr1.AB, tr1.BC, tr1.CD, tr1.AD))
print('Это трапеция?')
if tr1.check() == True:
    print('Да, это трапеция:')
    print('ее периметр равен: ', tr1.perimeter())
    print('а площадь: ', tr1.square())
else:
    print('нет, это не трапеция!')



