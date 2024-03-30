# Operadores Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 / 3)
print(10 // 3)
print(2 ** 3)

print('Hola ' + 'Python' + ' ¿Que tal?')
print('Hola ' + str(5))
print('Hola ' * 5)

# Operadores comparativos

print(3 > 4)
print(3 >= 4)
print(3 < 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print('-********************************')
print('')

print('Hola' > 'Python')
print('Hola' >= 'Python')
print('Hola' < 'Python') # Ordenación alfabética por ASCII
print('Hola' <= 'Python')
print('Hola' == 'Python')
print('Hola'!= 'Python')
print('Hola'== 'Hola')
print(len('Hola') > len('aa'))

# Operadores logicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 > 4 and "Hola" > "Python") or (3 > 4 and "Hola" > "Python")

print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")

print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))

# Operaciones aritméticas en Python

# Integers

print('Suma: ', 1 + 2) # 3
print('Resta: ', 2 - 1) # 1
print('Multiplicación: ', 2 * 3) # 6
print('Division: ', 6 / 2) # 3.0 Division in Python  gives floating number
print('Division: ', 7 / 2) # 3.5
print('Division without remainder: ', 7 // 2) # 3, gives without the floating number or without the remaining
print('Division without remainder: ', 7 // 3)  # 2
print('Módulo: ', 6 % 2) # 0
print('Potencia: ', 2 ** 3) # 8

# Floats

print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers


print('Complex Number, 1 + 2j', 1 + 2j)
print('Multiplying Complex Number,', (1 + 1j) * (1 - 1j))

# Example

a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a %  b
floor_division = a // b
exponential = a ** b

print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Example 2

# Calculating area of circle
radius = 10                             # radius od cirlce
pi = 3.14                               # valor de pi
area_of_circle = pi * radius ** 2       # two * sign menas exponent or power
print('Area of circle: ', area_of_circle)

# Calculating area of rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print('Weight of an object: ', weight, 'N')

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print('Density of a liquid: ', density, 'kg/m^3')

# operadores is, is not, in, not in

print('1 is 1', 1 is 1)                 # True - porque ambos objetos son los mismos
print('1 is not 2', 1 is not 2)         # True - porque 1 no es 2
print('S in Samuel', 'S' in 'Samuel')   # True - porque el caracter S se encuentra en la cadena 'Samuel'
print('I in Samuel', 'I' in 'Samuel')   # False - porque el caracter I no se encuentra en la cadena 'Samuel'
print('I not in Isaias', 'I' not in 'Isaias') # False - porque el caracter I si se encuentra en la cadena Isaias

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# Declare your age as integer variable
age : int =  27
print(age)

# Declare your height as float variable
height : float = 1.70
print(height)

# Declare a variable thar store coplex number
num_complex = (3 + 2j) * (3*3j + 2/8j)
print (num_complex)

