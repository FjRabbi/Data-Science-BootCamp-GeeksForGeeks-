print()
# ----------- Topic: Data Structure -----------
print("----------- Topic: Data Structure -----------")
print()

# ----------- List Introduction -----------
print("----------- List Introduction -----------")
print()

# Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
# In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.
#The list is a sequence data type which is used to store the collection of data. Tuples and String are other types of sequence data types.

var = ['geeks', 'for', 'geeks']
print(var)

# Python program to demonstrate
# Creation of List

# Creating a List

List = []
print("Blank List: ")
print(list)

# Creating a List of numbers
List = [10,25,78]
print('\nList of numbers: ')
print(List)

#Creating a list of strings and accessing using index
List = ['Geeks', 'for', 'geeks']
print("\nList Items: ")
print(List)
print(List[1])
print(List[2])


#In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list.
#The index must be an integer. Nested lists are accessed using nested indexing.

# Python program to demonstrate accessing of element from list
# Creating a List with the use of multiple values
List = ["Geeks", "For", "Geeks"]

# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])


# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]

# accessing an element from the Multi-Dimensional List using index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])




List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing an element using negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])

#Getting the size of the Python list
print()
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

print()

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List=[]
print("\nInitial Blank List: ")
print(List)

#Addition of Elements in the List
List.append(1)
List.append(23)
List.append(4)
List.append(56)
print("\nList after Addition of Three elements: ")
print(List)

print()
# Adding elements to the List using Iterator
for i in range(1,4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

#Adding tuples to the list
List.append((5,6))
print("\nList after addition of the Tuple: ")
print(List)


# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

#Python List insert() method inserts a given element at a given index in a list using Python.
# Syntax: list_name.insert(index, element)
# Parameters:
# index: the index at which the element has to be inserted.
# element: the element to be inserted in the list.
# Returns: Does not return any value.

#Python insert() method with string in Python.

lis = ['Geeks', 'Geeks']
lis.insert(1, "For")
print(lis)

print()

list1 = [1, 2, 3, 4, 5, 6, 7]
# insert 10 at 4th index
list1.insert(4, 10)
print(list1)

