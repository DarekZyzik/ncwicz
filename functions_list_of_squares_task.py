# Create a list of squares of first 10 integers:
# [1, 4, 9, ..., 100]

# **************
# Using 'for' loop:
# **************
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# place your code here
list1 = []
for i in numbers:
    i *= i
    list1.append(i)
print(list1)

# **************
# Using built-in 'map':
# **************

# place your code here
def square(n):
    return n * n

squared_numbers_iter = map(square, numbers)
print(list(squared_numbers_iter))

result = map(lambda x: x*x, numbers)
print(list(result))

# **************
# Using list comprehension:
# **************

# place your code here

new_list = [y*y for y in numbers]
print(new_list)






