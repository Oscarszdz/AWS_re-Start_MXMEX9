# Introducing the string data type
my_string = "This is a string."
print(f'Printing my_string variable. {my_string}')
print(f'Type of my_string value is {type(my_string)}')

# Working with string concatenation
first_string = "water"
second_string = 'fall'
third_string = first_string + second_string
print((third_string))

# Working with input strings
name = input("What is your name? ")
print(name)

# Formatting output strings
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")

print(f"{name}, you like a {color} {animal}!!")