# Sets #

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Initiallly it is a dictionary

my_other_set = {'Samuel', 'Calderón', 'Aguirre', 27}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('samcalderonaguirre')

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('samcalderonaguirre')

print(my_other_set) # Un set no admite repetidos

print('Samuel' in my_other_set)
print('Calderonn' in my_other_set)

my_other_set.remove('samcalderonaguirre')
print(my_other_set)


my_other_set.clear()
print(my_other_set)

del my_other_set # Función del sistema que elimina un objeto

my_set = {'Samuel', 'Calderón', 'Aguirre', 27}

my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))