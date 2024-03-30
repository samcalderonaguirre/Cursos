# Variables

my_variable = "My String variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_variable, my_int_variable, my_bool_variable)
print('Este es ek valor de:', my_bool_variable)

# Algunas funciones del sistema
print(len(my_variable)) # Contar la longitud de la variable u objeto

# Variables en una sola línea. ¡Cuidado con abusar de la sintaxis!
name, surname, alias, age = "Samuel", "Calderón", "samcalderonaguire", 27
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Entrada por teclado o Inputs
name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuántos años tienes?: ')

print(name)
print(age)

# Ejemplos de variables con la nomenclatura snake_case

first_name = 'Samuel'
last_name = 'Calderón'
country = 'Ecuador'
city = 'Machala'
age = 27
is_married = False
skills = ['Linux', 'reading', 'Python']
personal_info = {
    'firstname' : "Samuel",
    'lastname' : "Calderón",
    'country' : "Ecuador",
    'city' : "Machala",
    'age' : 27,
    'is_married' : False,
}

# Imprimir valores de variables

print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Is Married:', is_married)
print('Skills:', skills)
print('Personal Info:', personal_info)

# Conversion de tipos de datos

# int to float
num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float', num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 50
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int
num_str = '10'
print('num_int', int(num_str))
num_str = '10.84'
print('num_float', float(num_str))

# str to list
first_name = 'Samuel'
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)
