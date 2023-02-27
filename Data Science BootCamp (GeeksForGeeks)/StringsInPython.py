print()
# ----------- Strings in Python -----------
print("----------- Strings in Python -----------")
print()

# Python Program for
# Creation of String

# Creating a String
# with single Quotes
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ")
print(String1)

# Creating a String
# with double Quotes
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ")
print(String1)

# Creating a String
# with triple Quotes
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ")
print(String1)

# Creating String with triple
# Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''
print("\nCreating a multiline String: ")
print(String1)
print()
# ---------------------------- END ------------------------

# Python Program to Access
# characters of String

string1 = "Md. Fajle Rabbi Islam"
print("Print initial string: ", string1)

# Printing First character
print("First character of the string: ", string1[0])
# Printing Last character
print("Last character of the string: ", string1[-1])
print()
# ---------------------------- END ------------------------

# Program to reverse a string
print("Reverse of the string:", string1[::-1])
print()
# ---------------------------- END ------------------------

# Python Program to
# demonstrate String slicing

# Creating a String
String1 = "GeeksForGeeks"
print("Initial String: ")
print(String1)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(String1[3:-2])
print()
# ---------------------------- END ------------------------
# inbuilt function return an
# integer representing the Unicode code
value = ord("A")

# writing in ' ' gives the same result
value1 = ord('A')

# prints the unicode value
print(value, value1)
print()
# ---------------------------- END ------------------------

# The Python chr() function returns a string from a Unicode code integer.
print(chr(97))

print()
# ---------------------------- END ------------------------

print()
# ----------- Escape Sequencing in Python -----------
print("----------- Escape Sequencing in Python -----------")
print()

# Python Program for
# Escape Sequencing
# of String

# Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

# Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the
# use of Tab
String1 = "Hi\tGeeks"
print("\nTab: ")
print(String1)

# Printing Paths with the
# use of New Line
String1 = "Python\nGeeks"
print("\nNew Line: ")
print(String1)

print()
# ---------------------------- END ------------------------

print()
# ----------- String Operations Part (1) -----------
print("----------- String Operations Part (1) -----------")
print()

# in operator: The ‘in’ operator is used to check if a character/ substring/ element exists in a sequence or not.
# Evaluate to True if it finds the specified element in a sequence otherwise False.

s1 = 'geeksforgeeks'
s2 = 'geeks'
print(s2 in s1)
print(s2 not in s1)

print()
print()
# ---------------------------- END ------------------------
# String Concatenation using + Operator

var1 = "Riyad's mood is "
var2 = "sad right now"
var3 = var1 + var2
print(var3)

print()
# ---------------------------- END ------------------------
# Python String index() Method allows a user to find the index of the first occurrence of an existing substring inside a given string.

# Syntax:  string_obj.index(substring, begp, endp)
#
# Parameters:
# substring: The string to be searched for.
# begp (default : 0): This function specifies the position from where the search has to be started.
# endp (default: length of the string): This function specifies the position from where the search has to end.
# Return:  Returns the first position of the substring found.

indexVar = 'random'
print("Index of 'and' in string: ", indexVar.index('and'))

print()

# initializing target string
ch = "geeksforgeeks"

# initializing argument string
ch1 = "geeks"

# using index() to find position of "geeks"
# starting from 2nd index
# prints 8
pos = ch.index(ch1, 2)

print("The first position of geeks after 2nd index : ", end="")
print(pos)

print()
# ---------------------------- END ------------------------
# The index() method is similar to find().
# The only difference is find() returns -1 if the searched string is not found and index() throws an exception in this case.

test_string = "1234gfg4321"
# finding gfg in string segment 'gfg4'
print(test_string.index('gfg', 4, 8))

# finding "21" in string segment 'gfg4321'
print(test_string.index("21", 8, len(test_string)))

# finding "32" in string segment 'fg432' using negative index
print(test_string.index("32", 5, -1))

print()
# ---------------------------- END ------------------------
# Python String rindex() method returns the highest index of the substring inside the string if the substring is found.
# Otherwise, it raises ValueError.
# Example 1: Python String rindex() Method with start or end index
# If we provide the start and end value to check inside a string, Python String rindex() will search only inside that range.

string = "ring ring"

# checks for the substring in the range 0-4 of the string
print(string.rindex("ring", 0, 4))

# same as using 0 & 4 as start, end value
print(string.rindex("ring", 0, -5))

string = "101001010"
# since there are no '101' substring after string[0:3]
# thus it will take the last occurrence of '101'
print(string.rindex('101', 2))

string = "ring ring"

# search for the substring,
# from right in the whole string
print(string.rindex("ring"))

string = "geeks"
# this will return the right-most 'e'
print(string.rindex('e'))

print()
# ---------------------------- END ------------------------

print()
# ----------- String Operations Part (2) -----------
print("----------- String Operations Part (2) -----------")
print()


# Case Changing of Strings
# The below functions are used to change the case of the strings.
# lower(): Converts all uppercase characters in a string into lowercase.
# upper(): Converts all lowercase characters in a string into uppercase.
# title(): Convert string to title case.

def factorial(n):
    x = 1
    for i in range(1,n+1):
        fact = 1
        for j in range(1,x+1):
            fact *= j
        print(f'The factorial of {x} is :', fact)
        x += 1


factorial(25)

