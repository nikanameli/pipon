# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

number1 = int(input("Введите X1: "))
number2 = int(input("Введите Y1: "))
number3 = int(input("Введите X2: "))
number4 = int(input("Введите Y2: "))

result = ((number3 - number1) ** 2 + (number4 - number2) ** 2) ** (1/2)
print(result)
