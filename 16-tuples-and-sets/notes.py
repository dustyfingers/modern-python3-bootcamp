# tuples - and ordered collection of items - similar to a list with a few key differences. 
# the key difference is tuples are immutable!
# tuples are a bit faster and safer bug wise since they are unchanging...so  use them!
month_tuple = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# access like an array
month_tuple[1] # feb

# tuples can be used as keys in dictionaries
locations = {
    (35.7806,102.322542): 'Tokyo Office',
    (35.7809,102.322545): 'London Office',
    (35.7356,102.322548): 'San Francisco Office',
}

# iterating a tuple
for month in month_tuple:
    print(month)


# sets - like a formal math set. they DO NOT allow duplicate values. sets are unordered.
s = set({ 1, 4, 5, 7, 8, 9 })
set_too = { 2, 4, 6, 8, 10, 12 }

# set methods and set math
s.add('37b')
s.remove(4)
# s.remove('Moscow') # throws a keyerror
another_s = s.copy() # makes a copy of the data in the set
another_s.clear() # empties the set

# union of sets
union_set = s | set_too

# intersection of sets
intersection_set = s & set_too

# set comprehensions
print({x**2 for x in range(10)})
