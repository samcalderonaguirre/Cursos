### Conditionals ###

my_condition = True

if my_condition : # Es lo mismo que if my_condition == True
    print('Se ejecuta la condicion del if')

my_condition = 5 * 3

if my_condition == 10 : # Es lo mismo que if my_condition == True
    print('Se ejecuta la condicion del segundo if')

if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y  menor que 20')
elif my_condition == 25:
    print('Es igual a 25')
else:
    print('Es menor o igual que 10 o mayor o igual que 20')

print('La ejecución continúa')

my_string = 'Mi cadena de texto'

if my_string:
    print('Mi cadena de texto no está vacía')

a = 0
if a > 0:
    if a  % 2 == 0:
        print('A is a positive number an even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

print('\n################################\n')

a = 0
if a > 0 and a % 2 == 0:
    print('A is a even and positive integer')
elif a > 0 and a % 2!= 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

print('\n################################\n')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')