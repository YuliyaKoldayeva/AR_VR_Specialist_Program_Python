for number in range(26):
    print("{}: ".format(number), end="")
    if number%3 == 0:
        print("Fizz", end="")
    if number%5 == 0:
        print("Buzz", end="")
    print("")