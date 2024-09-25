# Problem statement
# You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.

# You don't need to print or return anything, just change in the input array itself.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1sec
# Sample Input 1:
# 1
# 6
# 9 3 6 12 4 32
# Sample Output 1 :
# 3 9 12 6 32 4
# Sample Input 2:
# 2
# 9
# 9 3 6 12 4 32 5 11 19
# 4
# 1 2 3 4
# Sample Output 2 :
# 3 9 12 6 32 4 11 5 19 
# # 2 1 4 3 

#code here
from sys import stdin


def swapAlternate(arr, n):
    length = len(arr)
    if n % 2 == 0:

        for i in range(0,length,2):


            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    else:
        for i in range(0,length-1,2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]






# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# Printing the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    if n != 0:
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1