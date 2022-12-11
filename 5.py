# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(2):
    for t in range(2):
        for j in range(2):
            print(i, t, j, end=': ')
            if (not (i or t or j)) == ((not i) and (not t) and (not j)):
                print('true')
            else:
                print('false')

