# Create a function, which takes range and returns list of square roots of odd integers from given range (do not use loops)

# put your code here

def square(x,y):
    z = [i**2 for i in range(x,y) if i%2 !=0]
    return (z)

print(square(3,9))
