# http://www.apache.org/licenses/LICENSE-2

# Exercises for conditionals

# Level 1

# 1: Get user input('Enter you age: '). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output

age = int(input('Enter your age ---> '))

if age >= 18:
    print('You are old enough to learn to drive')
else:
    print(f'You need {18 - age} years to learn to drive')

# 2: Compare the values of my_age and your_age using if... else. Who is older (me or you)? Use input('Enter your age: ') to get the age as input.
# You can use a nested condition to print  'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your age. Output

my_age = 27
your_age = int(input('Enter your age ---> '))
difference_age = abs(my_age - your_age)

if my_age == your_age:
    print('You are the same age as me')
elif my_age < your_age and difference_age == 1:
    print('You are one year older than me')
elif my_age < your_age and difference_age > 1:
    print(f'You are {difference_age} years older than me')
elif my_age > your_age and difference_age == 1:
    print('You are one year younger than me')
else:
    print(f'You are {difference_age} years younger than me')

# 3: Get two numbers from the user using input prompt. if a is  greater than b return a is a greater than b, if a is less b return a is smaller than b, else a is equals to b

a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equals to {b}')

# Level 2

# Write a code which gives to students according to theirs scores:

scores = {
    '90-100' : 'A',
    '70-89': 'B',
    '60-69' : 'C',
    '50-59' : 'D',
    '0-49' : 'F'
}

student_name = input('Enter your name: ')
student_score = int(input('Enter your score: '))

print(f'Student name -> {student_name}')

if student_score < 50:
    print(f"Your grade: {scores.get('0-49')}")
elif student_score >= 50 and student_score < 60:
    print(f"Your grade: {scores.get('50-59')}")
elif student_score >= 60 and student_score < 70:
    print(f"Your grade: {scores.get('60-69')}")
elif student_score >= 70 and student_score < 90:
    print(f"Your grade: {scores.get('70-89')}")
else:
    print(f"Your grade: {scores.get('90-100')}")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer.

month = input('Enter the month: -> ')

if month == 'September' or month == 'October' or month == 'November':
    print('Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('Spring')
elif  month == 'June' or month == 'July' or month == 'August':
    print('Summer')
else:
    print('Invalid month')