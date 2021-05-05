# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

# from collections import defaultdict
#
# persons = [{"name": "John", "age": 15},
#            {"name": "Jack", "age": 45}]
# age_by_names = defaultdict(list)
# len_name_by_names = defaultdict(list)
# ages = []
#
# for p in persons:
#     name = p['name']
#     age = p['age']
#     age_by_names[age].append(name)
#     len_name_by_names[len(name)].append(name)
#     ages.append(age)
#
# min_age = min(age_by_names)
# print('min_age:', *age_by_names[min_age])
#
# max_len_name = max(len_name_by_names)
# print('max_len_name:', *len_name_by_names[max_len_name])
#
# print('average:', sum(ages) // len(ages))

# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

# my_dict_1 = {"name": "Ray",
#              "age": 45,
#              "les": "Ry"}
# my_dict_2 = {"name": "Nick",
#              "job": "actor"}
# result = list(set(my_dict_1.keys()).intersection(set(my_dict_2)))
# print(result)
#--------Создать список из ключей, которые есть в первом, но нет во втором словаре.---------------------------------------------------------
y_dict_1 = {"name": "Ray",
             "age": 45,
             "les": "Ry"}
my_dict_2 = {"name": "Nick",
             "job": "actor"}

result_dict = {
    key: y_dict_1[key] for key in set(y_dict_1) - set(my_dict_2)
}
# result_dict = {}
result_dict.update(y_dict_1)
result_dict.keys()

print(result_dict)
# new_list = [mydict[k] for k in mykeys if k in mydict]
# print(new_list)

# -Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.-----------------------------------------------------------------------------------------

# y_dict_1 = {"name": "Ray",
#              "age": 45,
#              "les": "Ry"}
# my_dict_2 = {"name": "Nick",
#              "job": "actor"}
# res = dict((key, y_dict_1[key]) for key in y_dict_1 if key not in my_dict_2)
# print(res)