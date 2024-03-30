# Exercises: Level 1

# 1: Create an empty tuple
empty_tuple = ()

# 2: Create a tuple containing names of your sisters and your brothers
sisters = ('Isis', 'Iris', 'Mery')
brothers = ('Joseph', 'Bolívar', 'Gustavo')

# 3: Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4: How many siblings do you have?
print(len(siblings))

# 5: Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings[1] = 'Pedro'
siblings.append('Bolívar')
siblings.append('Fanny')
siblings = tuple(siblings)
family_members = tuple(siblings)
print(family_members)

# Exercises: Level 2

# 1: Unpack sblings and parents from familiy_members
siblings2 = family_members[0:6]
parents = family_members[6:]

print(siblings2)
print(parents)

# 2: Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('pear', 'apple', 'kiwi', 'lemon')
vegetables = ('potato', 'salad', 'green peas', 'carrot')
animal_products = ('Chuck pot roast', 'Hot dog', 'fish', 'Chuck steak', 'milk')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3: Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_lt) % 2 == 1:
    middle_item = food_stuff_lt[int(len(food_stuff_lt) / 2 - 0.5)]
else:
    middle_item = food_stuff_lt[int(len(food_stuff_lt) / 2 - 0.5) : int(len(food_stuff_lt) / 2 + 0.5)]

print(middle_item)

# 5: Slice out the first three items and the last three items from food_staff_lt list
tree_fisrt_elements_food_staff = food_stuff_lt[0:3]
tree_last_elements_food_staff = food_stuff_lt[-3:]

print(tree_fisrt_elements_food_staff)
print(tree_last_elements_food_staff)

# 6: Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7: Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# * Check if 'Estonia' is a nordic country 
print('Estonia' in nordic_countries)

# * Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)