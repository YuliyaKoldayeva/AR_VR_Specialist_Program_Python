print("First option")
for number in range (20):
    if number%2 == 1:
        print(number)

print("Second option")
for number in range (20):
    if number%2 != 0:
        print(number)

print("Third option")
for number in range (20):
    if number%2 == 0:
        continue
    print(number)