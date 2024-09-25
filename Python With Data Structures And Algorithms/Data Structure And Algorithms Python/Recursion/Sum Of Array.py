# Problem statement
# Given an array of length N, you need to find and return the sum of all elements of the array.

# Do this recursively.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^3
# Sample Input 1 :
# 3
# 9 8 9
# Sample Output 1 :
# 26
# Sample Input 2 :
# 3
# 4 2 1
# Sample Output 2 :
# 7

def sumArray(arr):
    # Please add your code here
    n = len(arr)
    if n == 1:
        return arr[0]
    sum = sumArray(arr[1:])
    return arr[0] + sum    

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))

