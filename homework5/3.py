# Создайте программу для игры в ""Крестики-нолики"".

sp = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
print(*sp, sep="\n")


def win(mass):
    for i in range(2):
        if mass[i][0] == mass[i][1] == mass[i][2] and mass[i][0] != "-":
            return mass[i][0]
        if mass[0][i] == mass[1][i] == mass[2][i] and mass[1][i] != "-":
            return mass[0][i]
    if mass[0][0] == mass[1][1] == mass[2][2] and mass[0][0] != "-":   
        return mass[0][0]
    if mass[2][0] == mass[1][1] == mass[0][2] and mass[2][0] != "-":   
        return mass[2][0]


def validate(mass, x, y):
    if not(0 <= x <= 2) or not(0 <= y <= 2):
        return False
    elif mass[x][y] != '-':
        return False
    return True


counter = 0
while True:
    while True:
        x, y = input('Ход крестика. Введите позиции через пробел').split()
        x = int(x)
        y = int(y)
        if not validate(sp, x, y):
            print('Вы ввели что-то не так:(')
        else:
            break
    sp[x][y] = 'x'
    print(*sp, sep="\n")
    if win(sp):
        print('Победа крестика!')
        break
    counter += 1
    if counter == 9:
        print('Ничья')
        break
    while True:
        x, y = input('Ход нолика. Введите позиции через пробел').split()
        x = int(x)
        y = int(y)
        if not validate(sp, x, y):
            print('Вы ввели что-то не так:(')
        else:
            break
    sp[x][y] = '0'
    print(*sp, sep="\n")
    if win(sp):
        print('Победа нолика!')
        break
    counter += 1

