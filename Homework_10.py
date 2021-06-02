import json
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
def read_json(data):
    with open(data, "r", encoding='utf-8') as file:
        result = json.load(file)
    return result

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def func(surname):
    return surname['name'].split()[-1]


def sort_by_surname(data):
    surname = sorted(data, key=func)
    sort_surname = sorted(data, key=abs(surname))
    print(sort_surname)


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
def sort_by_years(dict1):
    year = dict1["years"].split("–")[1]
    if len(year.split()) == 1:
        return int(year.split()[0][:-1])
    return -int(year.split(" ")[-2])



# 4. Написать функцию сортировки по количеству слов в поле "text"

def sort_len_text(data_list):
    info_text = data_list.get("text")
    return len(info_text)












