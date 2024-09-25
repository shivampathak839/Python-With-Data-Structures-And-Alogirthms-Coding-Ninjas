# Problem statement
# Print the following pattern for the given number of rows.

# Pattern for N = 5
#  1    2   3    4   5
#  11   12  13   14  15
#  21   22  23   24  25
#  16   17  18   19  20
#  6    7    8   9   10
# Input format : N (Total no. of rows)

# Output format : Pattern in N lines

# Sample Input :
# 4
# Sample Output :
#  1  2  3  4
#  9 10 11 12
# 13 14 15 16
#  5  6  7  8


import math

n = int(input())

for i in range(math.ceil(n/2)):

   for j in range(1,n+1):

       print(n*2*i + j ,end = " ")

   print()

for i in range(n//2,0,-1):

   for j in range(1,n+1):

       print(n*(2*i-1) + j , end = " ")

   print()