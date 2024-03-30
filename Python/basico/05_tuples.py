# Tuples #


# Definir una tupla
my_tuple = tuple()
my_other_tuple = ()

# Que es una tupla es un conjunto de valores de valores inmutables

my_tuple = (25, 1.77, 'Sam', 'Calderon')
my_other_tuple = ('Aguirre', 75.0, 'Machala', 'Ecuador')

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Sam'))
print(my_tuple.count('Aguirre'))
print(my_tuple.index('Calderon'))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined