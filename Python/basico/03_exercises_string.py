# Exercises Strings


# Exercise 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('{} {} {} {}'.format('Thirty', 'Days', 'Of', 'Python'))

# Exercise 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('{} {} {}'.format('Coding', 'For', 'All'))

# Exercise 3: Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Exercise 4: Print the variable company using print().
print(company)

# Exercise 5: Print the length of the company string using len() method and print().
print(len(company))

# Exercise 6: Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Exercise 7: Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Exercise 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Exercise 9: Cut(slice) out the first word of Coding For All string.
print(company.split()[0])

# Exercise 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.rindex('Coding'))
print(company.find('Coding'))
print(company.rfind('Coding'))

# Exercise 11: Replace the word coding in the string 'Coding For All' to Python.
company_replace = company.replace('Coding', 'Python')
print(company_replace)

# Exercise 12: Change Python for Everyone to Python for All using the replace method or other methods.
print(company_replace.replace('All', 'Everyone'))

# Exercise 13: Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# Exercise 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
challenge = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(challenge.split(', '))

# Exercise 15: What is the character at index 0 in the string Coding For All.
print(company[0])

# Exercise 16: What is the last index of the string Coding For All.
print(company[len(company) - 1])

# Exercise 17: What character is at index 10 in "Coding For All" string.
print(company[10])

# Exercise 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
python = "Python For Everyone"
print(f"{python[python.index('P')]}. {python[python.index('F')]}. {python[python.index('E')]}.")

# Exercise 19: Create an acronym or an abbreviation for the name 'Coding For All'.
coding = "Coding For All"
print(f"{coding[coding.index('C')]}. {coding[coding.index('F')]}. {coding[coding.index('A')]}.")

# Exercise 20: Use index to determine the position of the first occurrence of C in Coding For All.
print(coding.index('C'))

# Exercise 21: Use index to determine the position of the first occurrence of F in Coding For All.
print(coding.index('F'))

# Exercise 22: Use rfind to determine the position of the last occurrence of l in Coding For All People.
coding = 'Coding For All People'
print(coding.rfind('l'))

# Exercise 23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))

# Exercise 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print(sentence.rfind('because'))

# Exercise 25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))

# Exercise 26: Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.index('because'))

# Exercise 27: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace('because because because', ''))

# Exercise 28: Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))


# Exercise 29: Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))


# Exercise 30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.
company ='  Coding For All      '
print(company.strip())

# Exercise 31:'  Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

print('30DaysOfPython'.isidentifier()) # False
print('thirty_days_of_python'.isidentifier()) # True

# Exercise 32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
web_tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(web_tech)
print(result)

# Exercise 33: Use the new line escape sequence to separate the following sentences.
new_line_scape = '''I am enjoy this challenge.
I just wonder what is next.'''
print(new_line_scape)

# Exercise 34: Use a tab escape sequence to write the following lines.
title = 'Name\tAge\tCountry\tCity'
file = 'Samuel\t25\tEcuador\tMachala'
print(f'{title}\n{file}')

# Exercise 35: Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'radius = {radius}\nThe area of a circle with radius {radius} is {area} meters square')

# Exercise 36: Make the following using string formatting methods:
'''
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
num1 = 8
num2 = 6

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')