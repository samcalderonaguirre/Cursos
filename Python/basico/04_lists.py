### Listas - Lists ###

my_list =  list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)

print(len(my_list))

my_other_list = [27, 1.70, 'Samuel', 'Calderón']


print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])

print(my_other_list.count('Samuel'))
print(my_list.count(30))

# Asignación de variables con una lista

age, height, name, surname = my_other_list

print(age)
print(height)
print(name)

name, surname, age, height = my_other_list[2], my_other_list[3], my_other_list[0], my_other_list[1]

print(name)
print(surname)
print(age)
print(height)

# Concatenar dos listas

print(my_list + my_other_list)

my_other_list.append('Sam12Dev') # Insertar al final de la lista

print(my_other_list)

my_other_list.insert(1, 'Blanco') # Insertar en una posición determinada

print(my_other_list)

my_other_list.remove('Blanco') # Eliminar un elemento de la lista
print(my_other_list)

my_list.remove(30) # Elimina por un elemento que se conoce que está en la lista
print(my_list)

print(my_list.pop()) # Eliminar el último elemento, desapilar
print(my_list)

my_pop_element = my_list.pop(2) # pop() es para eliminar de la lista un elemento y retorna ese valor
print(my_pop_element)
print(my_list)


del my_list[2] # Eliminar un elemento de la lista sin retornar.  Elimina por índice

print(my_list)

my_new_list = my_list.copy() # copiar una lista a otra

my_list.clear()  # limpia toda la lista

print(my_list)

print(my_new_list)

my_new_list.reverse() # Invierte los elementos de la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos de la lista
print(my_new_list)

# Sublistas
print(my_new_list[1:3]) # [30, 35]

