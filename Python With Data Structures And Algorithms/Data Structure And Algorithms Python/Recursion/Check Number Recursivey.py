# Problem statement
# Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.

# Do this recursively.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^3
# Sample Input 1 :
# 3
# 9 8 10
# 8
# Sample Output 1 :
# true
# Sample Input 2 :
# 3
# 9 8 10
# 2
# Sample Output 2 :
# false

def checkNumber(arr, x):
    if x not in arr:
        return False
    
    if arr[0]==x:
        return True
    

    newarr = arr[1:]
    
    return checkNumber(newarr, x)

   

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
