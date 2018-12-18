word = ""
for number in range(26):
    word = str(number)+": "
    if number%3 == 0:
        word = word+"Fizz"
    if number%5 == 0:
        word=word + "Buzz"
    print(word)


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
b = 0

for a in a_list:

    print(str(b + 1) + ":", end=" ")

    if a % 3 == 0:
        print("Fizz", end="")

    if a % 5 == 0:
        print("Buzz")
    else:
        print("")
    b = b + 1