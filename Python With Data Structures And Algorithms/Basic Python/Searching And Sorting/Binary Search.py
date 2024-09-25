# Problem statement
# You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'. Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.



# Note:
# You must write an algorithm whose time complexity is O(LogN)


# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^9
# 1 <= target <= 10^9
# Time Limit: 1 sec
# Sample Input 1:
# 7
# 1 3 7 9 11 12 45
# 3
# Sample Output 1:
# 1
# Explanation of sample output 1:
# nums = [1, 3, 7, 9, 11, 12, 45],
# The index of element '3' is 1.
# Hence, the answer is '1'.


# Sample Input 2:
# 7
# 1 2 3 4 5 6 7
# 9
# Sample Output 2:
# -1
# Explanation of sample output 2:
# nums = [1, 2, 3, 4, 5, 6, 7],
# Element '9' doesn't exist.
# Hence, the answer is '-1'.



from sys import stdin


def binarySearch(arr, n, x):
    
    n = len(arr)
    lower_bound = 0
    upper_bound =n-1
    
    while(lower_bound<=upper_bound):
        middle = (lower_bound+upper_bound)//2
        if x==arr[middle]:
            return middle
        elif x<arr[middle]:
            upper_bound=middle-1
        else:
            lower_bound = middle+1
    return -1


def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1

    
    
























