"""
Homework 1
FizzBuzz
1. Print a list of numbers from 0 to 25.
1. If the number is divisible by 3, print "Fizz".
2. If the number is divisible by 5, print "Buzz".
3. If the number is divisible by both, print "FizzBuzz"
"""

# Here is my first (the most concise & optimised) solution based on the multiplication property for strings
print("OUTPUT FOR THE FIRST SOLUTION")
for number in range(26):
    print("{}: {}{}".format(number,"Fizz"*(number%3==0),"Buzz"*(number%5==0)))


# Here is my second solution using string concatenation
print("OUTPUT FOR THE SECOND SOLUTION")
for number in range(26):
    word = str(number)+": "
    if number%3 == 0:
        word = word+"Fizz"
    if number%5 == 0:
        word=word + "Buzz"
    print(word)

# Here is my third solution using the parameter end=""
print("OUTPUT FOR THE THIRD SOLUTION")
for number in range(26):
    print("{}: ".format(number), end="")
    if number%3 == 0:
        print("Fizz", end="")
    if number%5 == 0:
        print("Buzz", end="")
    print("")
