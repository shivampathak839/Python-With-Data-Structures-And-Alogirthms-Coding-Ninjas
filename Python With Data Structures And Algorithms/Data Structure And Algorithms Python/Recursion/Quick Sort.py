# Problem statement
# Given the 'start' and the 'end'' positions of the array 'input'. Your task is to sort the elements between 'start' and 'end' using quick sort.



# Note :
# Make changes in the input array itself.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 6 
# 2 6 8 5 4 3
# Sample Output 1 :
# 2 3 4 5 6 8
# Sample Input 2 :
# 5
# 1 2 3 5 7
# Sample Output 2 :
# 1 2 3 5 7 
# Constraints :
# 1 <= N <= 10^3
# 0 <= input[i] <= 10^9


def partition(arr, start, end):
    pivot = arr[start]
    c = 0
    for i in range(start, end+1):
        if arr[i] < pivot:
            c = c +1
    arr[start+c], arr[start] = arr[start], arr[start+c]
    pivot_index = start +c
    i = start
    j = end
    while i<j:
        if arr[i]<pivot:
            i = i+1
        elif arr[j]>=pivot :
            j -=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    return pivot_index                        
def quickSort(arr, start, end):
    # Please add your code here
    if start >= end:
        return 
    pivot_index = partition(arr, start, end) 
    quickSort(arr, start, pivot_index-1)
    quickSort(arr, pivot_index+1, end)
       


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
