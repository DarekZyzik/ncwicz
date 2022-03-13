### Create function that calculates Fibonacci sequence for given N:
      # Fib(0) == 0
      # Fib(1) == 1
      # Fib(N) == Fib(N-1) + Fib(N-2)

# **************
# Do it with iteration
# **************
# place your code here
fib = []
x = 50
for i in range(0, x):
    if i == 0:
        fib.append(i)
    elif i == 1:
        fib.append(i)
    else:
        y = fib[i-1] + fib[i-2]
        fib.append(y)

print(f'ciag Fibonnaciego = {fib} ')

# **************
# Do the same but using recursion
# **************
# place your code here

# a = []
#
# def fib(x):
#     for i in range(0, x):
#         y = i-1
#         return y
#
#     s = fib(i) + fib(i-1)
#     print(s)
#
#
# print(fib(10))












# **************
# Do the same but using iteration
# **************

# place your code here







