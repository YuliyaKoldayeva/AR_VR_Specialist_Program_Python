
def if_divisible(number,div):
    if number%div == 0:
        return True

for number in range(26):
    print("{}: ".format(number), end="")
    if if_divisible(number,3):
        print("Fizz", end="")
    if if_divisible(number,5):
        print("Buzz", end="")
    print("")


