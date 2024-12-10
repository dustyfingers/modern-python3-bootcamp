# list stores a collection of items - equivalent to an array in js
our_list = ['printer paper', 'towels', 'apples', 'shampoo', 'heavy cream', 'razors']

# accessing items from a list in python
our_list[0]

# for item in our_list:
#     print(item)

# list methods in python
our_list.append('mint')
our_list.insert(2, 'bulgur wheat')
our_list.extend(['eggs', 'milk', 'tomatoes'])

# gets rid of everything in list
# our_list.clear()
# our_list.pop(3) # takes in an index of item to remove
# our_list.remove('eggs') # takes in an item to remove

our_list.index('eggs') # takes an item and returns its index in an array
our_list.count('milk') # returns how many times a given input shows up in an array
our_list.sort() # sorts numbers numerically and strings alphabetically
our_list.reverse() # reverses the array
list_str = ' '.join(our_list) # concatenates given array into string with called upon string between items...string method
# print(list_str)

# list slicing uses square bracket operators, not a method per se
# list[start:stop:step]
# sliced_list = our_list[0:len(our_list):2] # slice every other item out of the array

# swapping items in list
our_list[0], our_list[1] = our_list[1], our_list[0]

for item in our_list:
    print(item)
