iterations = 0
for digit1 in range(2):
    print( digit1, "          from the first loop")
    for digit2 in range(2):

        print( digit1, digit2, "          from the first AND the second loop")

        for digit3 in range(2):
            iterations = iterations+1

            print(digit1,digit2,digit3, "          from the first , the second and third  loop")
            print("")
            print("")
            print("          WE HAVE FINISHED OUR ITERATION NUMBER ", iterations)
            print("")
            print("")


