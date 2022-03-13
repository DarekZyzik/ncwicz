# Create a function calculating sum for any number of integers given to that function as arguments

# put your code here

def suma(r):
        y = [x for x in range(1, r+1)]
        return sum(y)

print(suma(100))
