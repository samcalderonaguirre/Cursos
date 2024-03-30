# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# 1: Find the length of the set it_companies
print(f'length of the set it_companies is -> {len(it_companies)}')

# 2: Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3: Insert multiple IT companies at once to the set it_companies
it_companies.update(['Open AI', 'Red Hat', 'NVIDIA'])
print(it_companies)

# 4: Remove one of the companies from the set it_companies
it_companies.remove('Open AI')
print(it_companies)

# 5: What is the difference between remove and discard
# it_companies.remove('Open AI') # If the item is not found remove() method will raise errors
it_companies.discard('Red Hat') # Remove the element and this method doesn't raise errors
print(it_companies)

# Exercises Level 2

# 1: Join A and B
print(A.union(B))

# 2: Find A intersection B
print(A.intersection(B))

# 3: Is A subset of B
print(A.issubset(B))

# 4: Are A and B disjoint sets
print(A.isdisjoint(B))

# 5: Join A with B and B with A
print((A.union(B)).union(B.union(A)))
print(A.union(B))
print(B.union(A))

# 6: What is the symmetric difference between A and B
print(A.symmetric_difference(B))


# 7: Delete the sets completely
del it_companies
del A
del B

# Exercises Level 3

# 1: Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)
print(f'Length of list age -> {len(age)}\nLength of set age -> {len(age_set)}')
print(age)
print(age_set)

# 2: Explain the difference between the following data types: string, list, tuple and set

'''
Strings are a collection of data that allow the representation of text, a list is a modifiable collection of data that allows data manipulation, 
a tuple is an immutable collection that can be used to use values that do not need to be modified in an application. , 
sets are an unordered collection that does not allow repeated elements and is used for mathematical set exercises.
'''

# 3: I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = 'I am a teacher and I love to inspire and teach people'

sentence_set = set(sentence)

print(sentence_set)

