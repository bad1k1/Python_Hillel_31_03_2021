# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta"]
# resolt = []
# for index in range(len(my_list)):
#     value = my_list[index]
#     if index % 2:
#         value = value.upper()
#     resolt.append(value)
# print(resolt)

# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "2ddsa1"]
# resolt = []
# for index, value in enumerate(my_list):
#     if index % 2:
#         value = value[::-1]
#     resolt.append(value)
# print(resolt)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

# my_list = ["Asd", "Ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "2ddsa1"]
# resolt = []
# for symbol in my_list:
#     if symbol.isupper():
#         resolt.append(symbol)
#
# print(resolt)

my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "2ddsa1"]
resolt = []
for symbol in my_list:
    if symbol in "a":
        resolt.append(symbol)
result_str = "___".join(resolt)
print(resolt)
