x = input("Enter some number " )
y = input("Enter some other number " )

try:
    test_result = (int(x)/int(y))
except ZeroDivisionError:
    print("Division by zero is impossible")

except ValueError:
    print("Please enter ONLY some number")
except Exception:
    print("An unknown error")
else:
    print(test_result)
