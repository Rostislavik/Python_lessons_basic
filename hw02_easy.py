# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print ('Задача-1')

fruits = ["дыня", "манго", "абрикос", "яблоко"]
a = 1

for i in fruits:
    print('{}.{:>30}'.format(a, i))
    a += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


print ('Задача-2')

x = {1,2,4,5,6,7,8}
y = {9,0,5,6,7,8}
z = x - y
print (z)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


print ('Задача-3')

a = [4, 24, 75, 54, 88, 99, 43, 52, 98, 12, 20]
print("Начальный список:", a)
b = []
for i in a:
    x = i % 2
    if x == 0:
        i = i / 4
    else:
        i = i * 2
    b.append(i)
print("Конечный список:", b)


