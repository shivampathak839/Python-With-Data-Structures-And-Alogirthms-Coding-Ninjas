# Problem statement
# You have been given a random integer array/list(ARR) of size N. You are required to find and return the second largest element present in the array/list.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 <= N <= 10^2
# 1<=arr[i]<=10^3

# Time Limit: 1 sec
# Sample Input 1:
# 5
# 4 3 10 9 2
# Sample Output 1:
# 9
# Sample Input 2:
# 7
# 13 6 31 14 29 44 3
# Sample Output 2:
# 31

# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    n = len(arr)
    
    if n==0:
        return -2147483648
    l =arr[0]
    s =0
    for i in range(1,n):
        if arr[i]>l:
            s = l
            l = arr[i]
        elif(arr[i]>s and arr[i]<l):
            s = arr[i]
        elif(arr[i]==l and arr[i+1]==l):
            for i in range(n):
                if arr[i]==l:
                    return -2147483648 

       
         
    return s



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(),0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
