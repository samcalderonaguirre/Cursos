# Exercises: Level 1

# Exercise1: Declare an empty list
empty_list = []

# Exercise2: Declare a list with more than five elements
list_items = ['Samuel', 'Calderón Aguirre', 27, 'Systems Engineer', 'Python Student', 'Machine Learning Student']

# Exercise3: find the length of your list
print(f'El tamaño de la lista es -> {len(list_items)}')

# Exercise4: Get the first item, the middle item and the last item of the list
print(f'El primer item de la lista es {list_items[0]}, el item del medio es {list_items[int(len(list_items) / 2 )]} y el último elemento es {list_items[-1]}')

# Exercise5: Declare a list called mixed_data_types, put your(name, age, height, marital_status, address)
mixed_data_types = ['Samuel', 27, 75.0, 'Soltero', 'Cdla. Brisas del Mar']

# Exercise6: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Exercise7: Print the list using print()
print(it_companies)

# Exercise8: Print the number of companies in the list
print(len(it_companies))

# Exercise9: Print the first, middle an the last company
print(f'{it_companies[0]}, {it_companies[int(len(it_companies) / 2)]}, {it_companies[-1]}')

# Exercise10: Print the list after modifying one of the companies
it_companies[0] = 'Canonical'
print(it_companies)

# Exercise11: Add an IT company to in it_companies
it_companies.append('Red Hat')

# Exercise12: Insert an IT company in the middle of it_companies
it_companies.insert(int(len(it_companies) / 2), 'Meta')

# Exercise13: Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# Exercise14: Join the it_companies with string '# '
it_companies_backup = it_companies.copy()
it_companies = '# '.join(it_companies)

# Exercise15: Check if a certain company exits in the it_companies list
company_exits = 'Microsoft' in it_companies
print(it_companies)
print(company_exits)

# Exercise16: Sort the list using sort() method
it_companies = it_companies_backup.copy()
it_companies.sort()
print(it_companies)

# Exercise17: Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Exercise18: Slice out the first 3 companies from the list.
del it_companies[0:3]
print(it_companies)

# Exercise19: Slice out the last 3 companies from the list.
del it_companies[-3:]
print(it_companies)

# Exercise20: Slice out the middle IT company or companies from the list.
del it_companies[1]
print(it_companies)

# Exercise21: Remove the first IT company from the list}
it_companies.remove('Meta')
print(it_companies)

# Exercise22: Remove the middle IT company or companies from the list
it_companies.remove('Google')
print(it_companies)
it_companies = it_companies_backup.copy()

# Exercise23: Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Exercise24: Remove all IT companies from the list
it_companies = it_companies_backup.copy()
it_companies.clear()
print(it_companies)

# Exercise25: Destroy the IT companies list
del it_companies

# Exercise26: Join the following list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

front_end.extend(back_end)

# Exercise27: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.append('Python')
full_stack.append('SQL')

print(full_stack)

# Exercises: Level 2

# Exercise1: The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# * Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages)
print(f'El minimo de edad es {min_age} y el máximo de edad es {max_age}')

# * Add the min age and the max age again to the list.
ages.append(min_age)
ages.append(max_age)

# * Find the median age (one middle item or two middle items divided by two)
ages.sort()
len_ages = len(ages)
if len_ages % 2 == 0:
    median_age = (ages[int(len_ages / 2) - 1] + ages[int(len_ages / 2)]) / 2
else:
    median_age = ages[int(len_ages / 2)]
print(median_age)

# * Find the average age (sum of all items divided by their number)
sum_age = 0
for i in ages:
    sum_age += i
avg_age = sum_age / len(ages)

print(avg_age)

# * Find the range of the ages (max minus min)
max_age = max(ages)
min_age = min(ages)
range_age = max_age - min_age

print(f'max_age -> {max_age}, min_age -> {min_age}, range_age -> {range_age}')

# * Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_age - avg_age) == abs(max_age - avg_age))
print(abs(min_age - avg_age) > abs(max_age - avg_age))
print(abs(min_age - avg_age) < abs(max_age - avg_age))

# Exercise1: Find the country(ies) in the countries list
from data.countries import countries

countries_list = countries.copy()
middle_country = countries_list[int(len(countries_list) / 2)]

print(f'middle country in the countries list -> {middle_country}')

# Exercise2: Divide the countries list into two equal lists if it is even if not one more country for the first half.
#countries_list = countries.copy()
if len(countries_list) % 2 == 0:
    first_half = countries_list[0:int(len(countries_list) / 2)]
    second_half = countries_list[int(len(countries_list) / 2):]
else:
    first_half = countries_list[0:int(len(countries_list) / 2) + 1]
    second_half = countries_list[int(len(countries_list) / 2) + 1:]

print(f'len first half list -> {len(first_half)}, len second half list -> {len(second_half)}')

# Exercise3: ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

# 1
potencies = []
scandic_countries = []

potencies.append(countries_list[countries_list.index('China')])
potencies.append(countries_list[countries_list.index('Russia')])
potencies.append(countries_list[countries_list.index('United States')])

scandic_countries.append(countries_list[countries_list.index('Finland')])
scandic_countries.append(countries_list[countries_list.index('Sweden')])
scandic_countries.append(countries_list[countries_list.index('Norway')])
scandic_countries.append(countries_list[countries_list.index('Denmark')])

print(f'potencies -> {potencies}')
print(f'scandic_countries -> {scandic_countries}')

# 2
countries_list2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china, russia, usa, *scandic_countries_list2 = countries_list2

print(f'china -> {china}, russia -> {russia}, usa -> {usa}, scandic_countries_list2 -> {scandic_countries_list2}')