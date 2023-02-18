
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')
student("Md. Fajle Rabbi", "Islam" )
print()


# ---------------------------- END ------------------------

# Python program to illustrate
# *args for variable number of arguments


def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
print()


# ---------------------------- END ------------------------

# A simple Python function to check
# whether x is even or odd

def evenOdd(x):
    """Function to check if the number is even or odd"""


    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)

print()
# ---------------------------- END ------------------------

def square_value(num):
    """This function returns the square value of the entered number"""
    return num ** 2

print(square_value.__doc__)
print(square_value(2))
print(square_value(-4))
print()
# ---------------------------- END ------------------------

# Pass by Reference or pass by value
# One important thing to note is, in Python every variable name is a reference. When we pass a variable to a function, a new reference to the object is created.

# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)
print()
# ---------------------------- END ------------------------


