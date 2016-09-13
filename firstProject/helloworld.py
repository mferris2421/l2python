# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')     #ask the user for their name

myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?')      #ask the user for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

print('I am ' + str(25) + " years old.")

spam = input()
spam = int(spam)
