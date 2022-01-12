import math
def override(x):
    x = print("Don't cheat!")

math.factorial = override
# your code here

# don't delete this line, please
math.factorial(23)
