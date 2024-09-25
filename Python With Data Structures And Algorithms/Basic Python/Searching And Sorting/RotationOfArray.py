# Problem statement
# You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).

#  Note:
# Change in the input array/list itself.You don't need to return or print the elements.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^4
# 0 <= N <= 10^6
# 0 <= D <= N
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output 1:
# 3 4 5 6 7 1 2
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7
# 0
# 4
# 1 2 3 4
# 2
# Sample Output 2:
# 1 2 3 4 5 6 7
# 3 4 1 2


from sys import stdin


def rotate(arr, n, d):

    #Your code goes here
    n = len(arr)
    arr[:]=arr[d:n] + arr[0:d]

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1

