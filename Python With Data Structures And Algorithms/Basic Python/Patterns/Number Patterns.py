# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1
# 11
# 111
# 1111
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input :
# 5
# Sample Output :
# 1
# 11
# 111
# 1111
# 11111


## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
p = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(p, end="")
        j +=1
    print()
    i +=1
    
        
