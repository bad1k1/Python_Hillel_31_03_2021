###################################exercise_1

my_list = [1, 2, 5, 8, 12, 123, 542, 343, 6777]

for my_list in my_list:
    if my_list > int(100):
        print(my_list)

###################################exercise_2

my_list = [1, 2, 5, 8, 12, 123, 542, 343, 6777, 2134]
my_results = []

for my_results in my_list:
    if my_results > int(100):
        print(my_results)

###################################exercise_3

my_list = [1,123, 1234, 565, 565, 665, 5653, 543,454]
new_list = my_list + [0] if len(my_list) <= 2 else my_list[7] + my_list[8]
print(new_list)


###################################exercise_4


my_string = "0123456789"
my_string_2 = "0123456789"
for symb_1 in my_string:
	for symb_2 in my_string_2:
		new_list = [int(symb_1+symb_2)]
		print(new_list)

