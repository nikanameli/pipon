number = int(input("Введите порядковый номер дня недели: "))
if number > 0 and number < 6:
    print("Будний день.")
elif number < 0 or number > 7:
    print("Введенное число не соответсвует задаче.")
else: 
    print("Выходной")