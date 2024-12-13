instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'blah_blah_blah': 'stuff here'
}

# access data in dictionary
# print(instructor['name'])

# iterating a dict in python
for value in instructor.values():
    print(value)

for key in instructor.keys():
    print(key)

for key, value in instructor.items():
    print(key, value)

# the in keyword and dicts
"name" in instructor.keys() # True
'Bill' in instructor.values() # false

# dict methods
# clear
# instructor.clear() # empties out the dictonary

# copy
x = instructor.copy() # returns a copy of the dictionary

# fromkeys creates a dict with the given keys and value
y = ['stuff', 'goes', 'here']
z = 0
new_dict = dict.fromkeys(y, z)
print(new_dict)

# get
a = new_dict.get('stuff')
print(a)

# pop
# new_dict.pop('goes')

# popitem - removes something random from the dictionary?? weird
# new_dict.popitem()

# update - creates a new dictionary from a dictionary...will give all props from 
new_new_dict = new_dict.update()