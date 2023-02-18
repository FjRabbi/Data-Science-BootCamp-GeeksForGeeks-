

print("---------- Declaring print, declaring variables & input ---------")

print("Ich bin Fajle Rabbi. Und Ich bin klug :)")

print("GFG ist die beste Plattform fur DSA-Inhalte", end="**")
print("Welcome to GFG")

a=b=c=10

print(a)
print(b)
print(c)

a =24

print(a)

p,q,r = 12,45.89, "Reaponsibility"

print(p)
print(q)
print(r)


#n = int(input("Enter the size of the list: "))

#lst = list(map(int, input("Enter the integer numbers of list separated by space").strip().split()))[:n]
#print("The List is: ",lst)

print("\n\n")


# --------------- Arithmatic Operation ----------------

# Operator	Description	Syntax
# "+"	Addition: adds two operands	x + y
# "–"	Subtraction: subtracts two operands	x – y
# "*"	Multiplication: multiplies two operands	x * y
# "/"	Division (float): divides the first operand by the second	x / y
# "//"	Division (floor): divides the first operand by the second	x // y
# "%"	Modulus: returns the remainder when first operand is divided by the second	x % y
# "**"  Power : Returns first raised to power second	x ** y

print("--------------- Arithmatic Operation ----------------")

val1 = 17
val2 = 3

print(val1+val2)
print(val1-val2)
print(val1*val2)
print(val1/val2)
print(val1%val2)
print(val1**val2)
print(val1//val2)


print("\n\n")


print("----------- Type -----------")

A1 = ('MD', 'FAJLE', 'RABBI', 'ISLAM')
A2 = ["MD", "FAJLE", "RABBI", "ISLAM"]
A3 = {"MD":1, "FAJLE":2, "RABBI":3, "ISLAM":4}
A4 = "MD. FAJLE RABBI ISLAM"
A5 = 18
A6 = 18.05

print(type(A1))
print(type(A2))
print(type(A3))
print(type(A4))
print(type(A5))
print(type(A6))

print(type([]) is list)

print(type([]) is not list)

print(type(()) is tuple)

print(type({}) is dict)

print(type({}) is not list)


print("----------- Type Conversion-----------")

# s = "10101"
#
# c = int(s,2)
# print("After converting to integer base 2: ", end="")
# print(c)
#
# e = float(s)
# print(e)

p= 'A'
c = ord(p)  # ord() return the ascii code of any character as inter type
print(type(c), c)

h = hex(c)  # hex() return the hexadecimal number of any integer as string type
print(type(h) ,h)

o = oct(c)  # oct() return the octal number of any integer as string type
print(type(o), o)


# tuple() : This function is used to convert to a tuple.
# set() : This function returns the type after converting to set.
# list() : This function is used to convert any data type to a list type.

# using  tuple(), set(), list()

# initializing string
s = 'geeks'

# printing string converting to tuple
c = tuple(s)
print("After converting string to tuple : ", end="")
print(c)

# printing string converting to set
c = set(s)
print("After converting string to set : ", end="")
print(c)

# printing string converting to list
c = list(s)
print("After converting string to list : ", end="")
print(c)

# dict() : This function is used to convert a tuple of order (key,value) into a dictionary.
# str() : Used to convert integer into a string.
# complex(real,imag) : This function converts real numbers to complex(real,imag) number.

# Python code to demonstrate Type conversion
# using  dict(), complex(), str()

# initializing integers
a = 1
b = 2

# initializing tuple
tup = (('a', 1), ('f', 2), ('g', 3))

# printing integer converting to complex number
c = complex(1, 2)
print("After converting integer to complex number : ", end="")
print(c)

# printing integer converting to string
c = str(a)
print("After converting integer to string : ", end="")
print(c)

# printing tuple converting to expression dictionary
c = dict(tup)
print("After converting tuple to dictionary : ", end="")
print(c)

# chr(number): This function converts a number to its corresponding ASCII character.
# Convert ASCII value to characters
a = chr(76)
b = chr(77)

print(a)
print(b)





