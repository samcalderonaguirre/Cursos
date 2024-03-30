#Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.1416
r = float(input('Ingrese el radio del circulo '))
pi = 3.1416

area = pi * pow(r, 2)
circumference = 2 * pi * r

print('El area del circulo es', area)
print('La circunferencia del círculo es', circumference)