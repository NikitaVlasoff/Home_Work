def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append([])

        for j in range(m):
            matrix[i].append(value)

    print(matrix)
    return matrix

n = int(input('Введите кол-во строк: '))
m = int(input('Введите кол-во столбцов: '))
value = input(f'Значение матрицы: ')
print('-------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Введено некорректное значение строк!')
elif m <= 0:
    print('Введено некорректное значение столбцов!')
else :
    print('Результат: ')
    for i in matrix:
        print(*i)
