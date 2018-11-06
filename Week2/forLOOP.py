# First type
for t in range (11):
    asteriscs = t*"*"
    print("{} : {}".format(t,asteriscs))


print("First program run has ended")

# Second type
for t in range (11):
    print(str(t) + " : ", end="")
    for i in range (t):

        print("*", end="")
    print("")


print("Second program run has ended")

