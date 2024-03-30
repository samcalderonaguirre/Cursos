# Dia 2: 30 días de progrmación en Python

# Declaración de variables
first_name = 'Samuel'
last_name = 'Calderón'
full_name = 'Samuel Isaías Calderón Aguirre'
country = 'Ecuador'
city = 'Machala'
age = 27
year = 2024
is_married = False
is_true = True
is_light_on = False

# Declarar múltiples variables en una línea
num_int, num_float, num_string, current_year, current_month = 12, 13.58, '23.66', 2024, 'March'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(num_int))
print(type(num_float))
print(type(num_string))
print(type(current_year))
print(type(current_month))

print('la longitud de la variable first_name es:', len(first_name))
print('La longitud de la variable first_name es:', len(first_name), '. La longitud de la variable last_name es:', len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, '=', num_one, '+', num_two)
print(diff, '=', num_two, '-', num_one)
print(product, '=', num_two, '*', num_one)
print(division, '=', num_one, '/', num_two)
print(remainder, '=', num_two, '%', num_one)
print(exp, '=', num_one, '**', num_two)
print(floor_division, '=', num_one, '//', num_two)

# Ejercicio con el area del circulo
radius_circle = 30
area_of_circle = 3.14 * radius_circle ** 2
circum_of_circle = 3.14 * radius_circle * 2

print(area_of_circle, '=', 3.14 * radius_circle ** 2)
print('circum_of_circle', '=', 3.14, '*', radius_circle,'**', 2)

radius_circle = input('Ingrese el radio del circulo: ')
area_of_circle = 3.14 * float(radius_circle) ** 2
print(area_of_circle)

first_name = input('Ingrese el primer nombre: ')
last_name = input('Ingrese el apellido: ')
country = input('Ingrese el país: ')
age = input('Ingrese la edad: ')

print(first_name)
print(last_name)
print(country)
print(age)