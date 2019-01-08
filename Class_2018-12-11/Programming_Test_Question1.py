# Number guessing game
import random


def ask_user(guess_counter):
    user_number = int(
        input("Please enter some integer number between 1 - 100 (attempt {}, you have {} more attempts) >> ".format(guess_counter, 6-guess_counter)))
    return user_number


secret_number = random.randint(1,100)

print("Let's play. Try to guess my secret number.")
guess_counter = 1
user_number = ask_user(guess_counter)


while guess_counter < 6:

    if user_number == secret_number:
        break

    if user_number > secret_number:
        print("Too hight, try again >> ")

    if user_number < secret_number:
        print("Too low, try again >> ")

    guess_counter = guess_counter + 1
    user_number = ask_user(guess_counter)


if user_number == secret_number:
    print ("Congrats! The secret number is {}".format(secret_number))

else:
    print("GAME OVER. Sorry, you didn't guess")