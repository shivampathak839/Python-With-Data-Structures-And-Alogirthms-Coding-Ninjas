# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# A
# BC
# CDE
# DEFG
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints
# 0 <= N <= 13
# Sample Input 1:
# 5
# Sample Output 1:
# A
# BC
# CDE
# DEFG
# EFGHI
# Sample Input 2:
# 6
# Sample Output 2:
# A
# BC
# CDE
# DEFG
# EFGHI
# FGHIJK
## Read input as specified in the question
## Print the required output in given format
## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while (i <= n):
    j = 1
    start_char = chr(ord("A") + i - 1)
    while (j <= i):
        char_p = chr(ord(start_char) + j - 1)
        print(char_p, end="")
        j = j + 1
    print()
    i =i+ 1

