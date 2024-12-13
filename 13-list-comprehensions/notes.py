our_list = ['apples', 'bananas', 'oranges']
nums = [1,2,3,4,5,6,7,8,9,10]

new_nums = [x*10 for x in nums]
doubled_nums = [x*2 for x in nums]
cubed_nums = [x**3 for x in nums]

print(new_nums)
print(doubled_nums)
print(cubed_nums)

string = 'herlloooooo'

char_arr = [x.upper() for x in string]
print(char_arr)

# conditional logic
evens = [num for num in nums if num % 2 == 0]
print(evens)

odds = [num for num in nums if num % 2 != 0]
print(odds)
