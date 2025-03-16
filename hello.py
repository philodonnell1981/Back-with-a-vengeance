# This program says hello and asks for my name.
print('Hello, world!')
print('What is your name?') # Asks their name.
my_name = input('>')
print('It is nice to me you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('What is your age?') # Asks for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.') # converts str to int to calculate and then back to str to print.
