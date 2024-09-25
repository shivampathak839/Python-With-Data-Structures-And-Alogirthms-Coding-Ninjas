# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 202
# 3003
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= n <= 50
# Output format :
# Pattern in N lines
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 202
# 3003
# 40004
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while(i<=n):
    j = 0
    while j<i:
        print(0 if j and j<i-1 else i-1 or 1, end="")
        j +=1
    print()
    i+=1
        