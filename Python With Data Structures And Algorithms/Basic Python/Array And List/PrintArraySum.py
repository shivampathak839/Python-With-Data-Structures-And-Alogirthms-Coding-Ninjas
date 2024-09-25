# Problem statement
# Given an array of length N, you need to find and print the sum of all elements of the array.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^6
# Note for C++:
# It is advisable to declare an array with a size that can accommodate all the elements, considering that N has a maximum value of 10^5.
# Sample Input :
# 3
# 9 8 9
# Sample Output :
# 26


#code 
n = int(input())
li= [int(x) for x in input().split()]

add = 0
for ele in li:
    add=add + ele
print(add)
