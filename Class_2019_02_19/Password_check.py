import re


def validate_password_complexity:
password_accepted = False

while not password_accepted:

    users_password = input("Choose your password : ")

    if not re.search("[\w]{8,}", users_password):
        print("Your password should be at least 8 characters long")
    else:
        password_accepted = True


    if not re.search("[0-9]{1,}", users_password):
        print("Your password should have at least 1 digit")
    else:
        password_accepted = True


    if not re.search("[a-z]{1,}", users_password):
        print("Your password should have at least 1 lower case")
    else:
        password_accepted = True

    if not re.search("[A-Z]{1,}", users_password):
        print("Your password should have at least 1 upper case")
    else:
        password_accepted = True


    if not re.search("[!,@,#,$,%,^,&,*]{1,}", users_password):
        print("Your password should have at least 1 special character")
    else:
        password_accepted = True

