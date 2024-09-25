# Problem statement
# Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.



#  Note:
# Change in the input array/list itself. 


# Example:
# Input:
# N = 5
# arr = {8, 6, 2, 5, 1}

# Output:
# 1 2 5 6 8 
# Explanation: add-image

# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 6
# 2 13 4 1 3 6 
# Sample Output 1:
# 1 2 3 4 6 13 
# Explanation Of Sample Input 1:
#  Select 1 and swap with element at index 0. arr= {1,13,4,2,3,6}

#  Select 2 and swap with element at index 1. arr= {1,2,4,13,3,6}

#  Select 3 and swap with element at index 2. arr= {1,2,3,13,4,6}

#  Select 4 and swap with element at index 3. arr= {1,2,3,4,13,6}

#  Select 6 and swap with element at index 4. arr= {1,2,3,4,6,13}
# Sample Input 2:
# 5
# 9 3 6 2 0
# Sample Output 2:
# 0 2 3 6 9
# Constraints :
# 1 <= N <= 10^3
# 0 <= arr[i] <= 10^5
# Time Limit: 1 sec


#code herer

from sys import stdin

def selectionSort(arr, n) :
    #Your code goes here
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
                
        arr[i],arr[min]=arr[min], arr[i]
    return arr



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
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1

