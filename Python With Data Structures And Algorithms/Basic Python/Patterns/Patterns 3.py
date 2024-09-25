# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 121
# 1221
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 121
# 1221
# 12221
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while (i <= n):
    j = 0
    while j < i:
        print(2 if j and j < i - 1 else 1 , end="")
        j += 1
    print()
    i += 1
