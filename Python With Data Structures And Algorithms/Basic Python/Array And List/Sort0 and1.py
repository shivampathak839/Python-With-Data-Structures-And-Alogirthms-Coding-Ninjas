# Problem statement
# You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra array/list.

# Note:
# You need to change in the given array/list itself. Hence, no need to return or print anything. 
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 0 1 1 0 1 0 1
# Sample Output 1:
# 0 0 0 1 1 1 1
# Sample Input 2:
# 2
# 8
# 1 0 1 1 0 1 0 1
# 5
# 0 1 0 1 0
# Sample Output 2:
# 0 0 0 1 1 1 1 1
# 0 0 0 1 1 


from sys import stdin


def sortZeroesAndOne(arr, n):
    n = len(arr)
    type0 = 0
    type1 = n - 1
     
    while(type0 < type1):
        if(arr[type0] == 1):
            (arr[type0],
             arr[type1]) = (arr[type1],
                            arr[type0])
            type1 -= 1
        else:
            type0 += 1




# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1