# 1. Дано целое число (int). Определить сколько нулей в этом числе.

namber = 1002000
my_namber = str(namber).count("0")
print(my_namber)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

namber = 1002000
my_namber = len(str(namber)) - len(str(int(str(namber)[::-1])))
print(my_namber)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [2, 5, 7, 9, 3]
my_list_2 = [1, 8, 6, 3, 4]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
new_list = my_list[1:] + my_list[:1]
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

example = "43 больше чем 34 но меньше чем 56"
parts = example.split()
result = []
for value in parts:
    if value.isdigit():
        result.append(int(value))
res = sum(result)
print(res)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
l_index = my_str.find(l_limit)
r_index = my_str.rfind(r_limit)
result = my_str[l_index + 1 : r_index]
print(result)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str = 'abcde'
if len(my_str) % 2:
    my_str += "_"
result = []
for index in range(len(my_str) // 2):
    index = index * 2
    new_str = my_str[index: index + 2]
    result.append(new_str)
print(result)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2,4,1,5,3,9,0,7]
res = 0

for index in range(len(my_list)):
    if index in [0, len(my_list) - 1]:
        continue
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        res += 1
print(res)
