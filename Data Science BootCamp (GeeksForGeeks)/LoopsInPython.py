

#----------- Python While Loop-----------
print("----------- Python While Loop-----------")


mul=1
while(mul <= 10):
    print(5*mul, end =" ")
    mul = mul+1

print("\n")
# checks if list still
# contains any element

a = [1,2,3,4,5,6]

while a:
    print(a.pop(), end=" ")
print('\n')

count = 1
while count < 5 : count += 1 ; print("I will be a billionaire")

print("\n")


#----------- range() in Python -----------
print("----------- range() in Python -----------")

for i in range(6):
    print(i, end=" ")
print()


# range (stop) takes one argument.
# range (start, stop) takes two arguments.
# range (start, stop, step) takes three arguments.


for i in range(5, 10):
    print(i, end=" ")
print()


for i in range(5, 225, 20):
    print(i, end=" ")
print("\n\n")


#----------- For Loop In Python -----------
print("----------- For Loop In Python -----------")

# Iterating over a list
l = ["geeks", "for", "geeks"]
for i in l:
    print(i, end= " ")
print("\n")


# Iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['Md Fajle Rabbi Islam'] = 12317
d['Md Abdullah Al Mahmud'] = 12316
d['Nishat Anzum Nova'] = 12132


for i in d:
    print("% s % d"% (i,d[i]))
print("\n")

# Iterating over a String
print("String Iteration")
S = "Confidence"
for i in S:
    print(i, end=" ")
print("\n")


# ----------- Break In Python -----------
print("----------- Break In Python -----------")

i = 0

for i in range (10):
    if i==5 :
        break
    print(i, end=' ')
print("\nOut of the loop")


word="input()"
for letter in word:
    if letter =='(' or letter == 'e':
        break
    print(letter, end=' ')
print('\nLoop ends here')

print("\n\n")
# ----------- Continue In Python -----------
print("----------- Continue In Python -----------")

for var in "SherlockHolmes":
    if var == 'e':
        continue

    print(var, end='')

print("\n")
# ----------- Nested Loop in Python -----------
print("----------- Nested Loop in Python -----------")




for i in range(7,13,2):
    for j in range(1,11):
        print(f'{i} * {j}  = {i*j}')
    print('\n')


list1 = ['I am', "You are"]
list2 = ['healty', 'smart', 'intelligent', 'geek']

for i in list1:
    print(f'Start outer for loop')
    for j in list2:
        print(f'{i} {j}')
    print(f'End the loop')

# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

# Store length of list2 in list2_size
list2_size = len(list2)

# Running outer for loop to
# iterate through a list1.
for item in list1:

    # Printing outside inner loop
    print("start outer for loop ")
    # Initialize counter i with 0
    i = 0
    # Running inner While loop to
    # iterate through a list2.
    while (i < list2_size):
        # Printing inside inner loop
        print(item, list2[i])
        # Incrementing the value of i
        i = i + 1
    # Printing outside inner loop
    print("end for loop ")


# ----------- Problem of this chapter -----------
print("----------- Problem of this chapter -----------")

#Problem 1:
print("Square")
def square(s):
    for i in range(s):
        for j in range(s):
            if i==0 or j==0:
                print("* ", end='')
            elif i==s-1 or j ==s-1 :
                print("* ", end='')
            else:
                print("  ", end='')
        print()


s = 6 #int(input())
square(s)


print('\n')

#Problem 2:
print("Square Wall")
def squareWall(s):
    for i in range(s):
        for j in range(s):
                print("* ", end='')
        print()


s = 6 #int(input())
squareWall(s)


print('\n')


#Problem 3:
print("Right Triangle Wall")
def rightTriangleWall(s):
    for i in range(s+1):
        for j in range(i):
            print("* ", end='')
        print()


s = 6 #int(input())
rightTriangleWall(s)



print('\n')
#Problem 4:
print("Right Triangle")
def rightTriangle(s):
    for i in range(s+1):
        for j in range(i):
            if j == 0:
                print("* ", end='')
            elif j == i-1:
                print("* ", end='')
            elif i == s:
                print("* ", end='')
            else:
                print("  ", end = '')
        print()


s = 7 #int(input())
rightTriangle(s)



print('\n')
#Problem 5:
print("Inverted Right Triangle Wall")
def invertedRightTriangleWall(s):
    for i in range(s):
        for j in range(s):
            print("* ", end='')
        s -= 1
        print()


s = 6 #int(input())
invertedRightTriangleWall(s)



print('\n')
#Problem 6:
print("N sum")
def nsum(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    print(sum)


n = 10 #int(input())
nsum(n)


print('\n')
#Problem 7:
print("N Factorial")
def nFactorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *=i
    return ans


n = 10 #int(input())
x = nFactorial(n)
print(x)



print('\n')
#Problem 8:
print("Divisor")
def divisor(n):
    print('1', end=' ')
    for i in range(2,n):
        if n%i==0:
            print(i, end=' ')

    if(n!=1):
        print(n, end='')

n = 10 #int(input())
divisor(n)


print('\n')
#Problem 9:
print("Check Prime")
def checkPrime(n):

    if n==1: return False
    for i in range(2,n):
        if n%i==0:
            return False

    return True


n = 1231 #int(input())
x = checkPrime(n)
print(x)


print('\n')
#Problem 10:
print("Next Prime")
def nextPrime(n):

    if n<2: return 2
    else:
        if n%2 == 0: n+=1
        else: n+=2
        while True:
            for i in range(3,n+1,2):
                if i==n:
                    if n%i == 0: return n
                else:
                    if n%i == 0: n+=2


n = 47 #int(input())
x = nextPrime(n)
print(x)


print('\n')
#Problem 11:
print("Fibonacci")
def fibonacci(n):

    x = []
    y = 0
    z = 1
    x.append(z)
    for i in range (n):
        temp = y
        y = z
        z = z + temp
        x.append(z)

    return x[n-1]


n = 6#int(input())
x = fibonacci(n)
print(x)

print('\n')
#Problem 11:
print("GCD")
def gcd(a,b):

    if (a<b):
        a,b = b,a
    x = 1
    while x!= 0:
        if a%b == 0: return b
        else:
            temp = b
            b = a%b
            a = temp
        x = b

a = 11
b = 20 #int(input())
x = gcd(a,b)
print(x)


print('\n')
#Problem 12:
print("Capitalize and Count")
def capCount(s):

    n = s.upper()
    newString = ''
    x = 0
    count = 0
    for i in n:
        if x != 0:
            newString += (i.lower())
            if i == ' ': x = 0
            else: x +=1
        else:
            newString += i
            if i.isupper() : count +=1
            if i ==' ': x = 0
            else: x = 1
    print(newString)
    print(count)

s = "Bangladesh   is   c I love  you country"#int(input())
x = capCount(s)
print(x)


print()
#Problem Special:
print("Factorial Special")
def factorial(n):
    x = 1
    for i in range(1,n+1):
        fact = 1
        for j in range(1,x+1):
            fact *= j
        print(f'The factorial of {x} is :', fact)
        x += 1


factorial(25)

# ---------- End ---------- #
