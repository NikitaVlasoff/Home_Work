First = int(input('Число номер 1: '))
Second = int(input('Число номер 2: '))
Third = int(input('Число номер 3: '))
if First == Second and Second == Third and Third == Second: # and - строгий оператор, все условия должны соответсвовать.
    print(3) # 3 - Если все числа равны между собой.
elif First == Second or Second == Third or Third == Second: # or - или/или. Хотя бы одо значение должно подходить к условию.
    print(2) # 2 - Если хотя бы 2 из 3 введённых чисел равны между собой.
elif First != Second or Second != Third or Third != Second: # or - или/или. Хотя бы одо значение должно подходить к условию.
    print(0) # 0 - Если равных чисел среди 3-х вообще нет.

