# Problem statement
# You are given the starting 'l' and the ending 'r' positions of the array 'ARR'.



# You must sort the elements between 'l' and 'r'.



# Note:
# Change in the input array itself. So no need to return or print anything.
# Example:
# Input: ‘N’ = 7,
# 'ARR' = [2, 13, 4, 1, 3, 6, 28]

# Output: [1 2 3 4 6 13 28]

# Explanation: After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 1 2 3 4 6 13 28
# Explanation of Sample Output 1:
# After applying 'merge sort' on the input array, the output is [1 2 3 4 6 13 28].
# Sample Input 2:
# 5
# 9 3 6 2 0
# Sample Output 2:
# 0 2 3 6 9
# Explanation of Sample Output 2:
# After applying 'merge sort' on the input array, the output is [0 2 3 6 9].
# Constraints :
# 1 <= N <= 10^3
# 0 <= ARR[i] <= 10^9
def merge(a1,a2,arr):
    i =0
    j = 0
    k = 0
    while(i<len(a1) and j < len(a2)):
        if (a1[i]< a2[j]):
            arr[k] = a1[i]
            k = k+1
            i = i+1
        else:
            arr[k] = a2[j]
            k =k+1
            j = j+1
    while (i<len(a1)):
        arr[k] = a1[i]
        k = k+1
        i = i+1
    while (j< len(a2)):
        arr[k] = a2[j]
        j =j+1
        k=k+1







def mergeSort(arr):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return
    mid = len(arr)//2
    a1= arr[0:mid]
    a2 = arr[mid:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1,a2,arr)



# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)

