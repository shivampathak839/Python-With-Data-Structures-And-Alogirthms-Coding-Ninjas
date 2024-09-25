# Problem statement
# You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, merge them into a third array/list such that the third array is also sorted.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# 0 <= M <= 10^5
# Time Limit: 1 sec 
# Note:
# Consider the case when size of the two arrays is not same.
# Sample Input 1 :
# 1
# 5
# 1 3 4 7 11
# 4
# 2 4 6 13
# Sample Output 1 :
# 1 2 3 4 4 6 7 11 13 
# Sample Input 2 :
# 2
# 3
# 10 100 500
# 7
# 4 7 9 25 30 300 450
# 4
# 7 45 89 90
# 0
# Sample Output 2 :
# 4 7 9 10 25 30 100 300 450 500
# 7 45 89 90


from sys import stdin

def merge(arr1, n, arr2, m) : 
    #Your code goes here
    i,j=0,0
    n,m=len(arr1), len(arr2)
    new_array=[]
    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            new_array.append(arr1[i])
            i+=1
        else:
            new_array.append(arr2[j])
            j+=1
    while(i<n):
        new_array.append(arr1[i])
        i+=1
    while(j<m):
        new_array.append(arr2[j])
        j+=1
    return new_array

            

























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
