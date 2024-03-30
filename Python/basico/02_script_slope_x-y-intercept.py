# Calculate the slope, x-intercept, y-intercept the y = 2x - 2)
x = 0
y = 0

# x-intercept
x_intercept = (2 + y) / 2

# y-intercept
y_intercept = 2 * x - 2

# slope

m = (y_intercept - y) / (x - x_intercept)

print('Ecuacion: y = 2x + 2')
print('x-intercept: ', x_intercept)
print('y-intercept: ', y_intercept)
print('slope: ', m)

# Distancia euclidiana entre (2, 2) y (6, 10)
# Calcular la pendiente (slope) (m = (y2 - y1) / (x2 - x1)
# Distancia euclidiana = d(p, q) = sqrt(pow(p1 - q1, 2) + pow(p2 - q2, 2))

# (p1, p2) = (2, 2)
p1 = 2
p2 = 2

# (q1, q2) = (6, 10)
q1 = 6
q2 = 10

print('Los puntos (p1, p2) :', '(', p1, ',', p2, ').\nLos puntos (q1, q2) :', '(', q1, ',', q2, ')')

m2 = (q2 - p2) / (q1 - p1)

print('La pendiente es m = ', m2)

d_euclidiana = (pow(p1 - q1, 2) + pow(p2 - q2, 2)) ** 0.5

print('La distancia euclidiana es igual = ', d_euclidiana)

# Comparativa de pendientes

print('¿La pendiente m: ', m, 'y la pendiente m2:', m2, 'son iguales?', m == m2)

# Calculate the value of y (y = x² + 6x + 9). Try to use different x values and figure out at what x value y is going to be zero


x_1: int = -10
y_2: int = x_1 ** 2 + 6 * x_1 + 9

while y_2 != 0:
    x_1 += 1
    y_2 = x_1 ** 2 + 6 * x_1 + 9
    print(x_1, y_2)

# Find the length of 'python' and 'dragon' and make a falsy comparision statement.

print('La longitud de la palabra python: ', len('python'), '\nLa longitud de la palabra dragon: ', len('dragon'))
print(not(len('python') == len('dragon')))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Use and operator to check if on is found in both python and dragon')
print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python}
print('on' not in 'python' and 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
len_python = len('python')
len_python_float = float(len_python)
len_python_str = str(len_python_float)

print(len_python, '\n', len_python_float, '\n', len_python_str)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 23
es_divisible_cero = num % 2 == 0
print(es_divisible_cero)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print((7 // 3) is int(2.7))

# Check if type of '10' es equal to type of 10
print(type(10) == type('10'))

# Check if int('9.8') is equal to 10
print(int(float('9.8')) is 10)
print(int(float('9.8')))