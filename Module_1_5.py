#immutable_var = 1, 'a', 1.2, type
#print(immutable_var)
#immutable_var[1] = 3.9
#Tuple (кортеж) является неизменяемым типом данных. После того как мы создаем кортеж, в него нельзя добавлять, извлекать и изменять элементы

immutable_var_1 = 1, 'a', [1.2, type]
print(immutable_var_1)
immutable_var_1[2][0] = True
print(immutable_var_1)
# Если сам кортеж изменить нельзя, то он может хранить изменяемые типы данных с которыми можно взаимодействовать, как в этом случае.

mutable_list = [35, 'python', 256.43, type]
mutable_list.append('car') # 'append' - метод, который добавляет объект в конец списка.
mutable_list.extend('business') # 'extend' - метод добавления объекта по символам.
mutable_list[3] = int
mutable_list[5:13] = ('work')
del mutable_list[5:13] # 'del' - в этом случае данный оператор помог удалить объекты с помощью среза.
mutable_list.remove('car') # 'remove' - удаление из списка по названию объекта.
print('car' in mutable_list)
print(35 not in mutable_list)
print(mutable_list)
