# This program asks the user to enter their name and their age, printing out a message 
# addressed to them that tells them the year that they will turn 100 years old.

import datetime
now = datetime.datetime.now()
this_year = now.year

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
yrs_to_100 = 100 - age
year = this_year + yrs_to_100

num = int(input('Please enter a random number: '))

print((name + ' will turn to 100 years old in ' + str(year) + '\n') * num)