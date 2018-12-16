word = ""
for number in range(26):
    word = str(number)+": "
    if number%3 == 0:
        word = word+"Fizz"
        if number%5 == 0:
            word=word + "Buzz"
    print(word)