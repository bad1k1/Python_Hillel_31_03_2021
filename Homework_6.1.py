# # # 1. Дан список строк my_list. Создать новый список в который поместить
# # # элементы из my_list по следующему правилу:
# # # Если строка стоит на нечетном месте в my_list, то ее заменить на
# # # перевернутую строку. "qwe" на "ewq".
# # # Если на четном - оставить без изменения.
# # # Задание сделать с использованием enumerate или range.
# #
# #
# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "2ddsa1"]
# result = []
# for index, value in enumerate(my_list):
#     if index % 2:
#         value = value[::-1]
#     result.append(value)
# print(result)
#
# # # 2. Дан список строк my_list. Создать новый список в который поместить
# # # элементы из my_list у которых первый символ - буква "a".
# #
# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "ddsa"]
# result = []
# for symbol in my_list:
#     if symbol.startswith("a"):
#         result.append(symbol)
# print(result)
# #
# # # 3. Дан список строк my_list. Создать новый список в который поместить
# # # элементы из my_list в которых есть символ - буква "a" на любом месте.
# #
# #
# my_list = ["asd", "ydda", "ds", "ywq", "jsdqef", "andq", "fosta", "ddsa"]
# result = []
# for symbol in my_list:
#     if symbol.__contains__("a"):
#         result.append(symbol)
# print(result)
# #
# #
# # # 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# # # Создать новый список в который поместить только строки из my_list.
# #
# my_list = ["asd", "ydda", 32, "ds", "ywq", 543, "jsdqef", 17, "andq", "fosta", "ddsa"]
# result = [value for value in my_list if type(value) == str]
# print(result)
# #
# # # 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# # # которые встречаются в строке только один раз.
# my_str = "у лукоморья дуб зеленый, златая цепь на дубе том и днем и ночью кот ученый"
# my_set = set(my_str)
# my_list = []
# for letter in my_set:
#     if my_str.count(letter) == 1:
#         my_list.append(letter)
# print(my_list)


# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
# my_str = "у лукоморья дуб зеленый, златая цепь на дубе том и днем и ночью кот ученый"
# new_str = "Всё ходит по цепи кругом; Идёт направо — песнь заводит, Налево — сказку говорит"
# my_str_set = set(my_str)
# new_str_set = set(new_str)
# result = [my_str_set.intersection(new_str_set)]
# print(result)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = "abcds"
new_str = "abdds"
my_list = []
result = list(set(my_str).intersection(set(new_str)))
for letter in result:
    if my_str.count(letter) == 1 and new_str.count(letter) == 1:
        my_list.append(letter)
print(my_list)



# # 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# # Фамилия
# # Имя
# # Возраст
# # Проживание
# #     Страна
# #     Город
# #     Улица
# # Работа
# #     Наличие
# #     Должность
#
# person = {"Фамилия": "Панасюк",
#           "Имя": "Вадим",
#           "Возраст": 27,
#           "Проживание": {"Страна": "Украина",
#                          "Город": "Днепр",
#                          "Улица": "Солнечная"},
#           "Работа": {"Наличие": "Есть",
#                   "Должность": "PPC"}}
#
# # 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# # придумать и указать граммы для продуктов):
# # Составляющие
# #     Коржи
# #         Мука
# #         Молоко
# #         Масло
# #         Яйцо
# #     Крем
# #         Сахар
# #         Масло
# #         Ваниль
# #         Сметана
# #     Глазурь
# #         Какао
# #         Сахар
# #         Масло
# cake = {"Составляющие": {
#                           "Коржи": {
#                               "Мука": "100 гр",
#                               "Молоко": "300 мл",
#                               "Масло": "10 гр",
#                               "Яйцо": "9 шт",
#                           },
#                           "Крем": {
#                               "Сахар": "16 гр",
#                               "Масло": "38 гр",
#                               "Ваниль": "0.3 гр",
#                               "Сметана": "1010 гр",
#                           },
#                            "Глазурь": {
#                                "Какао": "300 гр",
#                                "Сахар": "80 гр",
#                                "Масло": "70 гр",
#                            }
# }}
# print(cake["Составляющие"]["Коржи"]["Мука"])