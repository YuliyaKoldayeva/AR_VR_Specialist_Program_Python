import os

mylist = os.listdir()
line_index = 0
my_dic = {}

for file_or_dir in mylist:

    line_index += 1
    my_dic[line_index] = file_or_dir


for key, value in my_dic.items():
    print(str(key)+ ": "+ value)



selected_by_user = int(input("Chose a file or a directory number >> "))

chosen_option = my_dic[selected_by_user]

if (os.path.isdir(chosen_option)):
    print("You've selected a directory")


if (os.path.isfile(chosen_option)):
    print("You've selected a file")
    with open(chosen_option, "r") as f1:
        print(f1.read())

