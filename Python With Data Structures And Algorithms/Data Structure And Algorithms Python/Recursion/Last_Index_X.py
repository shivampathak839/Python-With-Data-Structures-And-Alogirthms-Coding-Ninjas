# Problem statement
# Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.

# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.

# You should start traversing your array from 0, not from (N - 1).

# Do this recursively. Indexing in the array starts from 0.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^3

# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 3


## Read input as specified in the question.
## Print output as specified in the question.
def lastindex(a,x):
    l = len(a)
    if l==0:
        return -1
    smallerlist = a[1:]
    smalleroutput = lastindex(smallerlist,x)
    
    if smalleroutput != -1:
        return smalleroutput +1
    else:
        if a[0]==x:
            return 0
        else:
            return -1
        
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastindex(a, x))
        
        
        