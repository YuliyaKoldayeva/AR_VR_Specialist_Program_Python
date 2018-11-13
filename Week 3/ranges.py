# BREAK
print("Learning BREAK)")
for a in range(10):
    if a==3:
        break
    print(a)


# CONTINUE
print("Learning CONTINUE")
for a in range(10):
    if a==3:
        print("Number three should not be print")
        continue
    print(a)

print("Test for using the same variable")
b=5
for b in range(b):
    print(b)