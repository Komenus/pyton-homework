# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

check = True

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x and y and z)) != ((not x) or (not y) or (not z)):
                check = False
if check: 
    print('утверждение верно')                