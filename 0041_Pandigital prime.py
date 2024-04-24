# Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
# Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)

import itertools
import time
start_time = time.time()


def isprime(my_int):
    for i in range(2, int(my_int**(0.5)+1)):
        if my_int % i == 0:
            return False
    return True


my_list = list('987654321')

for i in range(0, 7):
    print(my_list)
    array = itertools.permutations(my_list)
    for eachpermutation in array:
        n = int(''.join(eachpermutation))
        if isprime(n) == True:
            print(n)
            break
    my_list.pop(0)

print(f'Execution time = {time.time()-start_time}')

#----------------------------------------------------------------------------------------
# # Permutation Method 1
# # Python function to print permutations of a given list

# def permutation(lst):
#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []

# # If there is only one element in lst then, only
# # one permutation is possible
#     if len(lst) == 1:
#         return [lst]

# # Find the permutations for lst if there are
# # more than 1 characters
#     l = []  # empty list that will store current permutation


# # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#         m = lst[i]
#         # Extract lst[i] or m from the list.  remLst is
#         # remaining list
#         remLst = lst[:i] + lst[i+1:]
#         # Generating all permutations where m is first element

#         for p in permutation(remLst):
#             l.append([m] + p)

#     return l
# # Driver program to test above function


# data = list('ABC')

# for p in permutation(data):
#     print(p)
#------------------------------------------------------------------------

#Permutation Method 2
# Python3 program to print all permutations with
# duplicates allowed

# def toString(List):
#     return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


# def permute(a, l, r):

#     if l == r:
#         print(toString(a))
#     else:
#         for i in range(l, r):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l+1, r)
#             a[l], a[i] = a[i], a[l]  # backtrack


# # Driver code
# string = list('ABC')
# n = len(string)
# a = list(string)
# # Function call
# permute(a, 0, n)
# ---------------------------------------------------------------------------------
