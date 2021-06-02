import random
import string

#
#
# # 1. Дан список строк my_list. Создать новый список в который поместить
# # # элементы из my_list по следующему правилу:
# # # Если строка стоит на нечетном месте в my_list, то ее заменить на
# # # перевернутую строку. "qwe" на "ewq".
# # # Если на четном - оставить без изменения.
# # # Задание сделать с использованием enumerate или range
#
#
# def create_list(my_list):
#     result = [value[::-1] if index % 2 else value for index, value in enumerate(my_list)]
#     return result
#
# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "2ddsa1"]
# result = create_list(my_list)
# print(result)
#
#
# # 2. Дан список строк my_list. Создать новый список в который поместить
# # # элементы из my_list у которых первый символ - буква "a".
#
# def create_a_symbol(my_list):
#     result = [symbol for symbol in my_list if symbol[0] =="a"]
#     return result
#
# # 3. Дан список строк my_list. Создать новый список в который поместить
# # # элементы из my_list в которых есть символ - буква "a" на любом месте.
#
# def create_a_symbol(my_list):
#     result = [symbol for symbol in my_list if "a" in set(symbol)]
#     return result
#
# # # 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# # # Создать новый список в который поместить только строки из my_list.
# #
#
# def create_list(my_list):
#     result = [value for value in my_list if type(value) == str]
#     return result
#
#
#
#  # 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# # # которые встречаются в строке только один раз.
#
#
# def create_list(my_str):
#     result = [letter for letter in my_str if my_str.count(letter) ==1]
#     return result
#
# # 6. Даны две строки. Создать список в который поместить те символы,
# # которые есть в обеих строках хотя бы раз.
#
#
# def create_list(my_str_1, my_str_2):
#     result = list(set([letter for letter in my_str_1 if my_str_2.count(letter) > 0]))
#     return result
#
# # 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# # но в каждой только по одному разу.
#
#
#
# def create_list(my_str_1, my_str_2):
#     result = [letter for letter in my_str_1 if my_str_1.count(letter) == 1 and my_str_2.count(letter) == 1]
#     return result


# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.



# def generate_email(names, domains):
#     rand_email = f"{random.choice(['king','miller','kean'])}.{random.randint(100,999)}@{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5, 8))}.{random.choice(['net','com','ua'])}"
#     return rand_email
#
#
#
# names = ["king", "miller", "kean"]
# domains = [".net", ".com", ".ua"]
# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "2ddsa1"]
# new_list = ["asd", "ydda", 32, "ds", "ywq", 543, "jsdqef", 17, "andq", "fosta", "ddsa"]
# my_str = "у лукоморья дуб зеленый, златая цепь на дубе том и днем и ночью кот ученый"
# my_str_1 = "abcd"
# my_str_2 = "abdd"


# return_1 = create_list(my_list)
# return_2 = create_a_symbol(my_list)
# return_3 = create_a_symbol(my_list)
# return_4 = create_list(my_list)
# return_5 = create_list(my_str)
# return_6 = create_list(my_str_1, my_str_2)
# return_7 = create_list(my_str_1, my_str_2)
return_8 = generate_email(names, domains)
print(return_8)






