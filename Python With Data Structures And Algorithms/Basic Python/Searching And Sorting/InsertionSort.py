# Problem statement
# You are given an integer array 'arr' of size 'N'.

# Note:
# Change in the input array itself. You don't need to return or print the elements.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 <= N <= 10^3
# 0 <= arr[i] <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 5
# 9 3 6 2 0
# Sample Output 1:
# 0 2 3 6 9
# Sample Input 2:
# 4
# 4 3 2 1
# Sample Output 2:
# 1 2 3 4 

from sys import stdin

def insertionSort(arr, n) :  
    #Your code goes here
    n = len(arr)
    for i in range(1,n):
        j=i-1
        temp = arr[i]
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
        

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    insertionSort(arr, n)
    printList(arr, n)

    t-= 1

