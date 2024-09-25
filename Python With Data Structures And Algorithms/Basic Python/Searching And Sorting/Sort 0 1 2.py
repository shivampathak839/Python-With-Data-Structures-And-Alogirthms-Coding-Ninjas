# Problem statement
# You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s. Write a solution to sort this array/list in a 'single scan'.

# 'Single Scan' refers to iterating over the array/list just once or to put it in other words, you will be visiting each element in the array/list just once.

# Note:
# 1. You need to change in the given array/list itself. Hence, no need to return or print anything. 
# 2. You are not allowed to sort the list/array directly.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 0 1 2 0 2 0 1
# Sample Output 1:
# 0 0 0 1 1 2 2 
# Explanation:  The array contains three 0s, two 1s, and two 2s. After sorting the array in a single scan, the 0s should come first, then the 1s, and finally the 2s. So the output is 0 0 0 1 1 2 2.
# Sample Input 2:
# 2
# 5
# 2 2 0 1 1
# 7
# 0 1 2 0 1 2 0
# Sample Output 2:
# 0 1 1 2 2 
# Explanation: The array contains one 0, two 1s, and two 2s. After sorting, the 0 comes first, then the 1s, and finally the 2s. So the output is 0 1 1 2 2.
# 0 0 0 1 1 2 2
# Explanation: The array contains three 0s, two 1s, and two 2s. After sorting, the 0s come first, then the 1s, and finally the 2s. So the output is 0 0 0 1 1 2 2.


from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    n = len(arr)
    i=0  
    countzero=0  
    countone=0  
    counttwo=0  
    while(i<n): 

        if (arr[i]==0):  
            countzero=countzero+1  
        elif (arr[i]==1):  
            countone=countone+1  
        else:  
            counttwo=counttwo+1  
        i=i+1  
    i=0  
    while(i<countzero): 

        arr[i]=0  
        i=i+1  
    i=countzero  
    while(i<countzero+countone):  
        arr[i]=1  
        i=i+1  
    i=countzero+countone  
    while(i<n):  
        arr[i]=2  
        i=i+1  
    return arr    



        


























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1

