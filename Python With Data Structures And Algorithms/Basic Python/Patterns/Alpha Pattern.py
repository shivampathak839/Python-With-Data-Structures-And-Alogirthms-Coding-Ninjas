# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 3
#  A
#  BB
#  CCC
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints
# 0 <= N <= 26
# Sample Input 1:
# 7
# Sample Output 1:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF
# GGGGGGG
# Sample Input 2:
# 6
# Sample Output 2:
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF


## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i  = 1
while(i<=n):
    j = 1
    char = chr(ord("A")+i-1)
    while(j<=i):
        print(char, end="")
        j +=1
    print() 
    i+=1