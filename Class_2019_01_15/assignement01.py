import os

dirname = "TestDir"

def create_dir_if_not_existing(name):

    if not os.path.isdir(name):
        os.mkdir(name)
        print("Directory " + name + " created.")

    else:

        print("Already exists")


create_dir_if_not_existing(dirname)



