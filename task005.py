# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# ВЫариант 1
#ax = float(input('Введите координаты точки A по оси x:'))
#ay = float(input('Введите координаты точки A по оси y:'))
#bx = float(input('Введите координаты точки B по оси x:'))
#by = float(input('Введите координаты точки B по оси y:'))
#import math
#s = math.sqrt((ax-bx)**2+(ay-by)**2)
#print('Растояние между точкой A до точки B =', round(s, 3))
# Вариант 2
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
ac = y1 - y2
bc = x2 - x1
print(round((ac ** 2 + bc ** 2) ** 0.5, 2))