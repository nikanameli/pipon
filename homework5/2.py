# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 100 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candies = 100
while candies > 0:
    n = int(input("Введите число конфеток: "))
    if(n > 28):
        print("Вы что-то напутали и взяли больше конфеток, чем положено.")
    else:
        candies = candies - n
        print(f"Осталось {candies} конфеток.")
        if (candies != 0):
            if (candies <= 28):
                print(f"Железяка победила, взяв {candies} конфет! Восстание машин не за горами...")
                break
            # b = randint(1, 28)
            b = candies % 29
            if b == 0:
                b = randint(1, 28)
            # if(b > candies):
            #     b = randint(1, candies)
            candies = candies - b
            print(f"Ход железяки, железяка взяла {b} конфет. Осталось {candies} конфеток")
        else:
            print("Победа человека! Осталось 0 конфет.")
