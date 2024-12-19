my_dict = {'Год рождения Пети': 2003, 'Возраст': 21,'Тел': 89617319607}
print(my_dict)
print(my_dict['Возраст'])
print(my_dict.get('Место рождения', 'Без ошибки')) # Проверка на численность в данном словаре. 'Без ошибки' - замещение none
print(my_dict)
my_dict.update({'Серия Паспорта' : 3217, 'Номер паспорта' : 535462}) #добавление Элементов через .update
print(my_dict)
del my_dict['Год рождения Пети'] # удаление элемента
print(my_dict)



my_set = {'level', 'support', 1, 20 , 1, 1, 'guys', 'level'} # множество
print(my_set)
print(my_set.update([4,5])) # Испрользовал комманду .update, а не .add, дабы не растягивать добаление элементов в 2 строки
print(my_set)
print(my_set.remove(4)) # удаление одного элемента
print(my_set)