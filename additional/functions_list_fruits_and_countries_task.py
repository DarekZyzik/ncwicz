# You have two lists: list of fruits and list of countries.
# Create a third list, containing pairs (tuples) of fruits and countries that start with same letter:

# place your code here
import Cython.Compiler.Naming

fruits = ['cherry', 'apple', 'melon', 'grape', 'pomelo', 'strawberry']
countries = ['vietnam', 'poland', 'sweden', 'india', 'canada', 'finland', 'denmark']

# **************
# Using 'for' loop:
# **************

# place your code here
t=()
T = []
for i in fruits:
    for j in countries:
        if i[0] == j[0]:
            t = (i,j)
            T.append(t)
print(T)

# **************
# Using list comprehension:
# **************

# place your code here
new_list = [(i,j) for i in fruits for j in countries if i[0] == j[0] ]
print(new_list)