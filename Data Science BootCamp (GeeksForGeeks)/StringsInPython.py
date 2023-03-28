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

# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())

# original string never changes
print("\nOriginal String")
print(text)
print()
# ---------------------------- END ------------------------


print(" Startswith & endswith Sequencing in Python ")
print()

# startswith() function is used to check whether a given Sentence starts with some particular string.
# Start and end parameter are optional.
# We may use them when we want only some particular substring of the original string to be considered for searching.

# Parameters :
# search_string : The string to be searched.
# start : start index of the str from where the search_string is to be searched.
# end : end index of the str, which is to be considered for searching.

# Example: str.startswith(search_string, start, end)
# The return value is binary. The functions returns True if the original Sentence starts with the search_string else False.



print(" Startswith & endswith Sequencing in Python ")
print()
# endswith() function is used to check whether a given Sentence ends with some particular string.
# Start and end parameter are optional.
# We may use them when we want only some particular substring of the original string to be considered for searching.

# Parameters :
# search_string : The string to be searched.
# start : start index of the str from where the search_string is to be searched.
# end : end index of the str, which is to be considered for searching.

# Example: str.endswith( search_string, start, end)
# The return value is binary. The functions returns True if the original Sentence starts with the search_string else False.


# Python code to implement startswith()
# and endswith() function.

str = "GeeksforGeeks"

# startswith()
print(str.startswith("Geeks"))
print(str.startswith("Geeks", 4, 10))
print(str.startswith("Geeks", 8, 14))

print("\n")

# endswith
print(str.endswith("Geeks"))
print(str.endswith("Geeks", 2, 8))
print(str.endswith("for", 5, 8))

print()
# ---------------------------- END ------------------------



print(" Split & Join  in Python ")
print()

# Python code
# to split and join given string

# input string
s = 'Geeks for Geeks'
# print the string after split method
print(s.split(" "))
# print the string after join method
print("-".join(s.split()))

print()
# ---------------------------- END ------------------------



print(" Strip  in Python ")
print()

# More methods are discussed in this article
# 1. strip():- This method is used to delete all the leading and trailing characters mentioned in its argument.
# 2. lstrip():- This method is used to delete all the leading characters mentioned in its argument.
# 3. rstrip():- This method is used to delete all the trailing characters mentioned in its argument.


# Python code to demonstrate working of
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"

# using strip() to delete all '-'
print(" String after stripping all '-' is : ", end="")
print(str.strip('-'))

# using lstrip() to delete all trailing '-'
print(" String after stripping all leading '-' is : ", end="")
print(str.lstrip('-'))

# using rstrip() to delete all leading '-'
print(" String after stripping all trailing '-' is : ", end="")
print(str.rstrip('-'))

print()
# ---------------------------- END ------------------------


print(" Find  in Python ")
print()

# Python String find() method returns the lowest index or first occurrence of the substring if it is found in a given string.
# If it is not found, then it returns -1.

# Parameters:
#sub: Substring that needs to be searched in the given string.
# start (optional): Starting position where the substring needs to be checked within the string.
# end (optional): End position is the index of the last value for the specified range. It is excluded while checking.

# Example: str_obj.find(sub, start, end)

# Return:  Returns the lowest index of the substring if it is found in a given string. If it’s not found then it returns -1.

word = 'geeks for geeks'
print(word.find('for'))

# If the start and end indexes are not provided then by default it takes 0 and length-1 as starting and ending indexes where
# ending indexes are not included in our search.
# The find() method is similar to index(). The only difference is find() returns -1 if the searched string is not found
# and index() throws an exception in this case.

# Example: find() With No start and end Argument

word = 'geeks for geeks'

# returns first occurrence of Substring
result = word.find('geeks')
print("Substring 'geeks' found at index:", result)

result = word.find('for')
print("Substring 'for ' found at index:", result)

# How to use find()
if word.find('pawan') != -1:
    print("Contains given substring ")
else:
    print("Doesn't contains given substring")

# Example: find() With start and end Argument

word = 'geeks for geeks'

# Substring is searched in 'eks for geeks'
print(word.find('ge', 2))

# Substring is searched in 'eks for geeks'
print(word.find('geeks ', 2))

# Substring is searched in 's for g'
print(word.find('g', 4, 10))

# Substring is searched in 's for g'
print(word.find('for ', 4, 11))


print()
# ---------------------------- END ------------------------


print()
# ----------- String Comparison in Python -----------
print("----------- String Comparison in Python -----------")
print()

# The relational operators compare the Unicode values of the characters of the strings from the zeroth index till the
# end of the string. It then returns a boolean value according to the operator used.

# “Geek” == “Geek” will return True as the Unicode of all the characters are equal

# In case of “Geek” and “geek” as the unicode of G is \u0047 and of g is \u0067
# “Geek” < “geek” will return True and
# “Geek” > “geek” will return False

print("Geek" == "Geek")
print("Geek" < "geek")
print("Geek" > "geek")
print("Geek" != "Geek")

print()
# ---------------------------- END ------------------------


# ----------- Problem of this chapter -----------
print("----------- Problem of this chapter -----------")
print()

print()
#Problem 1:
print("Reverse String")

def reverseString(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = 'Hello'
x = reverseString(s)
print(x)


# ---- Another way -----
def reverseString(s):
    return s[::-1]

s = 'Hello'
x = reverseString(s)
print(x)

# ---------------------------- END ------------------------

print()
#Problem 2:
print("Palindrome")

def isPalin(s):
    n = s.lower()
    x = n[::-1]
    if n == x:
        return True
    else:
        return False

s = 'TenEt'
x = isPalin(s)
print(x)


# ---------------------------- END ------------------------

print()
#Problem 3:
print("Find Pattern")
def findPattern(s,p):
    s = s.lower()
    p = p.lower()
    x = s.find(p)
    return x


s = 'TenEt'
p = 'pEt'
x = findPattern(s,p)
print(x)


# ---------------------------- END ------------------------

print()
#Problem 4:
print("Slice The String")
def sliceString(s):
    return  s[1:-1]

s = 'TenEt'
x = sliceString(s)
print(x)


# ---------------------------- END ------------------------

print()
#Problem 5:
print("Change Case")
def changeCase(s):
    print(s.title())
    print(s.upper())

s = 'TenEt'
x = changeCase(s)
print(x)



# ---------------------------- END ------------------------

print()
#Problem 6:
print("Print Alphabets")
def alphabets(c1,c2):
    o1 = ord(c1)
    o2 = ord(c2)
    for i in range(o1, o2+1):
        print(chr(i), end=' ')


c1 = '*'
c2 = 'z'
alphabets(c1,c2)