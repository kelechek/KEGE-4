num = 15
print(id(num))  # id() - выводит номер переменной в оперативной памяти

# Целое число / integer / int
my_int = 73
print(my_int, type(my_int))

# Дробные числа / вещественные числа / числа с плавающей точкой / float
my_float = 0.93
print(my_float, type(my_float))

# Строки / string / str
my_str_1 = 'he"nlo'
my_str_2 = "he'lo"
print(my_str_1, type(my_str_1))
print(my_str_2, type(my_str_2))

# Списки / list
my_list = [23, 64, 'henlo', 0.86]
print(my_list, type(my_list))

# Кортеж / tuple
my_tuple = ('Ivanov', 'Ivan', 59)
print(my_tuple, type(my_tuple))

# Множество / set
my_set = {1, 2, 3, 2, 1, 2, 3, 2, 2, 2, 1, 3}
print(my_set, type(my_set))

# Словарь / dictionary / dict
my_dict = {'name': 'Larisa', 'age': 91, 'lastname': 'Nesterova'}
print(my_dict, type(my_dict))

# Логический тип данных / boolean / bool
my_bool1 = True
my_bool2 = False
print(my_bool1, type(my_bool1))