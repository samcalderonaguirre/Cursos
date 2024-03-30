# Exercises of dictionary in Python

# 1: Crate an empty dictionary called dog
dog = {}

# 2: Add name, color, breed, legs, age to the dictionary
dog = {
    'name' : 'Blacki',
    'color' : 'black',
    'breed' : 'Labrador',
    'legs' : 4,
    'age' : 9
}

# 3: Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city, and address as keys, for the dictionary.

student = {
    'first_name' : 'Samuel',
    'last_name' : 'Calderón',
    'gender' :'male',
    'age' : 27,
    'marital_status' : 'single',
    'skills' : ['Linux', 'Python'],
    'country' : 'Ecuador',
    'city' : 'Machala',
    'address' : 'Av. Sargto Chica'
}

# 4: Get the length of the student dictionary
print(len(student))

# 5: Get the value of skills and check the data type, it should be a list.
print(student.get('skills'))
print(type(student.get('skills')))

# 6: Modify eh skills values by adding one or two skills.
student['skills'].append('Java')
student['skills'].append('C++')

# 7: Get the dictionary keys as a list
print(student.keys())

# 8: Get the dictionary values as a list
print(student.values())

# 9: Change the dictionary to a list of tuples using items() method
print(list(student.items()))
print(tuple(student.items()))

# 10: Delete one of the items in the dictionary
student.pop('address')
print(student)

# 11: Delete one of the dictionaries
del dog

