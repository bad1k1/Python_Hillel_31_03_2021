# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).



def take_data(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


def create_list_data(filename):
    res_list = [names[1:-1] for names in take_data(filename)]
    return res_list


#2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"


def take_data_sormane(filename):
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data



def create_surname_list(filename):
    res_list = [surname.split("\t")[1] for surname in take_data(filename)]
    return res_list

#3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)


def create_data_original_list(filename):
    with open(filename, "r") as txt_files:
        info_list = txt_files.readlines()
    info_list = [value.split(" - ")[0].split() for value in info_list if " - " in value]
    data_original_list = [value for value in info_list if len(value) == 3]
    return data_original_list



def create_data_modified_list(filename):
    data_modified_list = create_data_original_list(filename)
    for day in data_modified_list:
        day[0] = day[0].rstrip("nsthrd")
        if len(day[0]) == 1:
            day[0] = "0" + day[0]
        day[1] = month_dict[day[1]]
        data_modified_list = ["/".join(day) for day in data_modified_list]
    return data_modified_list



def create_list_data_dict(filename):
    list_data_dict = []
    data_original_list = create_data_modified_list(filename)
    data_origin_list = [" ".join(data) for data in data_original_list]
    data_modified_list = create_data_modified_list(filename)
    index = 0
    while index < len(data_original_list):
        dict_data = {"data_original" : data_origin_list[index], "data_modifiend": data_modified_list[index]}
        list_data_dict.append(dict_data)
        index += 1
        return list_data_dict



month_dict ={"January": "01",
             "February": "02",
             "March": "03",
             "April": "04",
             "May": "05",
             "June": "06",
             "July": "07",
             "August": "08",
             "September": "09",
             "October": "10",
             "November": "11",
             "December": "12"}


filename = "domains.txt"
domains_list = create_list_data(filename)

filename = "names.txt"
surnames_list = create_surname_list(filename)

filename = "authors.txt"
date_dict = create_list_data_dict(filename)
