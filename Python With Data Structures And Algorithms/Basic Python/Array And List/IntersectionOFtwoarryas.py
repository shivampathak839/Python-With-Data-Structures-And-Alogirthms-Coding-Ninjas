# Problem statement
# You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively. You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.

# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the first array/list(ARR1)


# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= M <= 10^3
# Time Limit: 1 sec 
# Sample Input 1 :
# 2
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7 
# 2
# 10 10
# 1
# 10
# Sample Output 1 :
# 2 4 3
# 10
# Sample Input 2 :
# 1
# 4
# 2 6 1 2
# 5
# 1 2 3 4 2
# Sample Output 2 :
# 2 1 2
# Explanation for Sample Output 2 :
# Since, both input arrays have two '2's, the intersection of the arrays also have two '2's. The first '2' of first array matches with the first '2' of the second array. Similarly, the second '2' of the first array matches with the second '2' if the second array.


# code

import sys


def intersections(arr1, n, arr2, m):

    lst = []
    n = len(arr1)
    m=len(arr2)
    for i in range(0,n):
        for j in range(0,m):
            if arr1[i] == arr2[j]:
                
                                   
                lst.append(arr1[i])
                arr2[j]="x"
                
                
                break

    temp = list((lst))
    for ele in temp:
        print(ele, end=" ")



# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1



