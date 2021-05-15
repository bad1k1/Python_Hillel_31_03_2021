# #1) У вас есть список my_list с значениями типа int.
# # Распечатать те значения, которые больше 100.
# # Задание выполнить с помощью цикла for.

my_list = [1, 2, 5, 8, 12, 123, 542, 343, 6777]

for my_list in my_list:
    if my_list > 100:
        print(my_list)

# #2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# # Добавить в my_results те значения, которые больше 100.
# # Распечатать список my_results.
# # Задание выполнить с помощью цикла for.

my_list = [1, 2, 5, 8, 12, 123, 542, 343, 6777, 2134]
my_results = []

for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

# #3) У вас есть список my_list с значениями типа int.
# # Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# # Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# # Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [1, 123, 1234, 565, 565, 665, 5653, 543, 454, 1]
if len(my_list) < 2:
    my_list.append(0)
else:
    new_list = my_list[-1] + my_list[-2]
    my_list.append(new_list)
print(my_list)


#4) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))

my_string = "0123456789"
new_string = []
for symb_1 in my_string:
    for symb_2 in my_string:
        new_string.append(int(symb_1 + symb_2))
print(new_string)

price_list = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 45}]
min_value_list = []
for price in price_list:
    min_value_list.append(list(price.values())[0])
min_value = max(min_value_list)
print(min_value)