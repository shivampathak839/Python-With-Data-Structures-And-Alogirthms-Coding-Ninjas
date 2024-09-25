# Problem statement
# You have been given an integer array/list(ARR) and a number X. Find and return the total number of pairs in the array/list which sum to X.

# Note:
# Given array/list can contain duplicate elements. 
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^3
# 0 <= X <= 10^9
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# Sample Output 1:
# 7
# Sample Input 2:
# 2
# 9
# 1 3 6 2 5 4 3 2 4
# 12
# 6
# 2 8 10 5 -2 5
# 10
# Sample Output 2:
# 0
# 2


#  Explanation for Input 2:
# Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.

# For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).

from sys import stdin


def pairSum(arr, n, x):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if i != j:



                if arr[i] + arr[j] == x:
                    count = count + 1



    return count


# Your code goes here


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1
