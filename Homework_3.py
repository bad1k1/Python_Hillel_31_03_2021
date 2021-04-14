###################################exercise_1

value = 100
new_value = value / 2 if value < 100 else - value
print(new_value)

###################################exercise_2

value = 10
new_value = 1 if value < 100 else 0
print(new_value)

###################################exercise_3

value = 104
new_value = "True" if value < 100 else "False"
print(new_value)

###################################exercise_4

my_str = "Homework3"
print(my_str[::2])

###################################exercise_5

my_str = "Homework3"
print(my_str[1::2])

###################################exercise_6

my_str = "task"
new_str = my_str + my_str if len(my_str) < 5 else my_str

print(new_str)

###################################exercise_7

my_str = "task"
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str

print(new_str)

