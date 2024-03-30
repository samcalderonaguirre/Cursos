### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
my_tab_line_string = "\tEste es un string con tabulación"
print(my_new_line_string)
print(my_tab_line_string)

my_scape_string = "\tEste es un string \nescapado"
print(my_scape_string)

# Formateo
name, surname, age = 'Samuel', 'Calderón', 27
print('Mi nombre es %s %s y mi edad es %d' % (name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = 'python'
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

# Reverse

language_reverse = language[::-1]
print(language_reverse)

# Funciones

print(language.capitalize()) # Primera letra en capital
print(language.upper()) # Todas en mayúsculas
print(language.lower()) # Todas en minúsculas
print(language.title()) # Titulo
print(language.count('o')) # Cantidad de o
print(language.find('o')) # Posición de o
print(language.isnumeric()) # Es numerico
print('1'.isnumeric())  # Es numerico
print(language.isalnum()) # Es alfanumérico
print(language.isalpha()) # Es alfabético
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith('py')) # language empieza por 'py'
print(language.startswith('Py')) # language empieza por 'Py'

# Multiline string is created by using triple single (''') or triple double quotes ("""")

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String concatenation

first_name = 'Samuel'
last_name = 'Calderón'
full_name = first_name + ' ' + last_name
print(full_name)

# Escape sequences in Strings
'''
* \n: new line
* \t: tab means(8 spaces)
* \\: backslash
* \': Single quote (')
* \": Double quote (")
'''

print('I hope everyone is enjoy the Python Challenge.\nAre you?')
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, world\"')

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'