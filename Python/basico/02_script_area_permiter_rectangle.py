# Cálculo del area de un triangulo
# Formula: area= length x width, perimeter = 2 x (length + width)

length = float(input('Ingrese el largo del triangulo: '))
width = float(input('Ingrese el ancho del triangulo: '))

area = length * width
perimeter = 2 * (length + width)

print('El area del triangulo es', area)
print('El perimetro del triangulo es', perimeter)