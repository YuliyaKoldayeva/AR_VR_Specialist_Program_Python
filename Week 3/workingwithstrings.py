init_string = input("Type any tiny text or phrase here using ! symbol.  >>>  ")
len_str = len(init_string)
print(init_string.upper())
print(init_string.title())
print(init_string.lower())
print("The length of the string is {}".format(len_str))
print(init_string.replace("!", "."))
print(init_string.upper().replace("!", "."))