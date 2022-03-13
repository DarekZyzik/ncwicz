# You have two lists, both randomly ordered: list of integers and list of string integers.
# Create a dictionary with numbers that match: {1: '1', 3: '3', 10: '10'}

integers = [3, 1, 4, 6, 10]
strings = ['1', '5', '10', '3']
# **************
# Using 'for' loop:
# **************

# place your code here
integer_map = map(int, strings)
string_to_int = list(integer_map)
integers.sort()
# print(string_to_int)
# print(integers)
diction = {}
i = 0
for x in integers:
    for y in string_to_int:
        if x == y:
            diction.update( {x : str(y)} )
            # print(f'{x} {y}')

            i += 1
        else:
            continue
print(diction)

# **************
# Using dict comprehension:
# **************

# place your code here



