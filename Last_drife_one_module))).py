my_list = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
my_set = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_dict = dict.fromkeys(['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']) #Создание словаря
print(my_dict)
my_dict['Johnny']= sum(my_list[0])/len(my_list[0]) #sum/len - сумма деленная на кол-во,для среднего значения

my_dict['Bilbo']= sum(my_list[1])/len(my_list[1]) #sum/len - сумма деленная на кол-во,для среднего значения

my_dict['Steve']= sum(my_list[2])/len(my_list[2]) #sum/len - сумма деленная на кол-во,для среднего значения

my_dict['Khendrik']= sum(my_list[3])/len(my_list[3]) #sum/len - сумма деленная на кол-во,для среднего значения

my_dict['Aaron']= sum(my_list[4])/len(my_list[4]) #sum/len - сумма деленная на кол-во,для среднего значения

print(my_dict)


