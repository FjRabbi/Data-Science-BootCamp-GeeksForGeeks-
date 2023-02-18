

#---------------------------------------
#def computepay(h, r):
#    if (h <= 40):
#       return (h * r)
#    else:
#        l = h - 40
#        extraRate = 10.5 * 1.5
#        epay = l * extraRate
#        opay = 40 * 10.5
#        tpay = epay + opay
#        return (tpay)

#h = float(input("Enter Hours:"))
#r = float(input("Enter Rates:"))
#p = computepay(h,r)
#print("Pay", p)
#-----------------------------------------



#tot = 0
#for i in [5, 4, 3, 2, 1] :
#    tot = tot + 1
#print(tot)


# --------------------------------------------

# count = 0
#
# while True:
#     num = input("Enter a number: ")
#     if(count == 0):
#         largest = int(num)
#         smallest = int(num)
#         count = 1
#     if num == "done":
#         break
#     try:
#         inum = int(num)
#     except:
#         print("Invalid input")
#         continue
#
#     if(inum > largest):
#         largest = inum
#
#     if(inum < smallest):
#         smallest = inum
#
# print("Maximum is", largest)
# print("Minimum is", smallest)


# --------------------------------------------

# Problem 1:
# Write a program to accept an amount and find the number of notes. Assume that, Available
# notes are 1000,500,100,50,10,5,1 please keep in mind that to find the answer, you have to
# consider the highest value as the first priority.

# Solution:

# X = input()
# x = int(X)
# t = 1000
# ht = 500
# h = 100
# fif = 50
# te = 10
# fi = 5
# o = 1
#
# print("Currency Count")
# f =  x//t
# m = x%t
# if f>0:
#     print("1000 ",f )
# f = m//ht
# m = m%ht
# if f>0:
#     print("500 ", f)
# f = m//h
# m = m%h
# if f>0:
#     print("100 ", f)
# f = m //fif
# m = m%fif
# if f>0:
#     print("50 ", f)
# f = m//te
# m %= te
# if f>0:
#     print("10 ", f)
# f = m//fi
# m %= fi
# if f>0:
#     print("5 ", f)
# f = m//o
# m %= o
# print("1 ", f)

# --------------------------------------------

# --------------------------------------------
# Problem 2:
# Find the prime number of an array.

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
#
# def find_primes(arr):
#     return [num for num in arr if is_prime(num)]
#
# array = list(map(int, input("Enter a list of numbers, separated by spaces: ").split()))
# print(find_primes(array))


# --------------------------------------------

# --------------------------------------------
# Problem 3:
# Find whether the string is palindrome of not?

# def is_palindrome(s):
#     if s == s[::-1]:
#         print("The string is palindrome")
#     else:
#         print("The string is not palindrome")
#
# x = input()
# is_palindrome(x)

# --------------------------------------------


# --------------------------------------------
# Problem 4:
# FizzBuzz: Write a program that prints the numbers from 1 to 100.
# But for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".


# for i in range(1,101):
#     if (i % 3 == 0 and i % 5 == 0 ):
#         print("FIzzBuzz")
#     elif (i % 3 == 0):
#         print("Fizz")
#     elif (i % 5 == 0):
#         print("Buzz")
#     else:
#         print(i)


# --------------------------------------------

# --------------------------------------------
# Problem 4: Reverse a string: Write a program that takes a string as input and returns the reverse of the string.
# def reverse_string(s):
#     return s[::-1]
#
# s = input()
# print(reverse_string(s))

# --------------------------------------------

# --------------------------------------------
# Problem 5: Longest common prefix: Write a program that takes an array of strings as input and
# returns the longest common prefix among all the strings in the array.

# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     if len(strs) == 1:
#         return strs[0]
#     strs.sort()
#     prefix = ""
#     for i in range(len(strs[0])):
#         if strs[0][i] == strs[-1][i]:
#             prefix += strs[0][i]
#         else:
#             break
#     return prefix
#
# print(longest_common_prefix(["flower", "flow", "flight"]))
# print(longest_common_prefix(["dog", "racecar", "car"]))
# print(longest_common_prefix([]))


#--------------------------------------------



# --------------------------------------------
# Problem 6:
# Two Sum: Write a program that takes an array of integers and a target integer as input,
# and returns the indices of two numbers in the array such that their sum is equal to the target.

# def two_sum(nums, target):
#     d = {}
#     for i, num in enumerate(nums):
#         if target - num in d:
#             return [d[target - num], i]
#         d[num] = i
#     return []
#
# print(two_sum([2, 7, 11, 15], 9))
# print(two_sum([3, 2, 4], 6))
# print(two_sum([3, 3], 6))

#-----------------------------------------------------


# --------------------------------------------
# Problem 6:
# Merge two sorted arrays: Write a program that takes two sorted arrays as input and returns a new sorted array
# that contains all the elements of both input arrays.


# def merge_sorted_arrays(arr1, arr2):
#     x = arr1 + arr2
#     return sorted(x)
#
# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
#
# print(merge_sorted_arrays(arr1,arr2))

#---------------------------------------------------

def max_profit(prices):
    left = 0
    right = 1
    maxProfit=0
    while right< len(prices):
        currentProfit = prices[right]-prices[left]
        if prices[left]<prices[right]:
            maxProfit = max(currentProfit, maxProfit)
        else:
            left = right
        right +=1
    return maxProfit

prices = list(map(int, input().split()))
print(max_profit(prices))


