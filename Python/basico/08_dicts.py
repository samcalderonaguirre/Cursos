### Dictionaries ###


my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    'Nombre' : 'Samuel',
    'Apellido' : 'Calderón',
    'Edad' : 27,
    1 : 'Python'
}

my_dict = {
    'Nombre' : 'Samuel',
    'Apellido' : 'Calderón',
    'Edad' : 27,
    'Lenguajes' : {'Python', 'Swift', 'Kotlin'},
    1 : 1.77
}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])
print(my_dict[1])

my_dict['Calle'] = 'Av. Sargto Chica'

print(my_dict)

del my_dict['Calle']
print(my_dict)

print('Samuel' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(('Nombre', 'Apellido', 1))

print(my_new_dict)

my_list = ['Nombre', 'Apellido', 'Edad', 1]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

print(list(my_dict.values()))

person = {
    'first_name': 'Samuel',
    'last_name': 'Calderón',
    'age': 27
}

print(person.get('first_name'))