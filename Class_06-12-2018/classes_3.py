class Cat:
    name = ""
    age=0
    registered = False


    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

        if input_age > 2:
            self.registered = True

    def meow(self, number_times):
        for number in range (number_times):
            print("Meow")

    def meow(self, number_times, frase):
        for number in range (number_times):
            print("Meow", frase)

c1 = Cat("Jack", 2)

c2 = Cat("Meow", 9)

print(str(c1.registered), str(c2.registered))

c1.meow(5)
