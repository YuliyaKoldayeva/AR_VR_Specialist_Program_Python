work_age = input("Enter the age you started to work ...")
real_age = input("Enter how old are you ...")
try:
    time_working = int(real_age) - int(work_age)
except ValueError:
    print("Your input is wrong")
except Exception:
else:
    print("You've been working for {} years".format(time_working))