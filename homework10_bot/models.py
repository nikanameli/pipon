import csv


def start(user_id, stones):
    with open('file.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', )
        users = list(reader)
    user_game = list(filter(lambda x: x[1] == str(user_id), users))
    if user_game:
        del users[int(user_game[0][0])]
        with open('file.csv', 'w', encoding='utf8', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for i, row in enumerate(users):
                row[0] = i
                writer.writerow(row) 
            writer.writerow([len(users), user_id, stones]) 
        return 1
    else:
        with open('file.csv', 'a', encoding='utf8', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([len(users), user_id, stones])
        return 0


def make_turn(user_id, count_of_stones):
    if count_of_stones > 13 or count_of_stones < 1:
        return False, 2
    with open('file.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', )
        users = list(reader)
    user_game = list(filter(lambda x: x[1] == str(user_id), users))
    if not user_game:
        return False, 1
    if user_game:
        if not int(user_game[0][2]):
            return False, 4
        id = int(user_game[0][0])
        if int(user_game[0][2]) < count_of_stones:
            return False, 3
        users[id][2] = str(int(users[id][2]) - count_of_stones)
        ost = users[id][2]
        with open('file.csv', 'w', encoding='utf8', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for i, row in enumerate(users):
                row[0] = i
                writer.writerow(row) 
        return True, int(ost)
