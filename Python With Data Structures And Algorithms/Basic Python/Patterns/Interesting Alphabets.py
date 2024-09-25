# Problem statement
# Print the following pattern for the given number of rows.

# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints
# 0 <= N <= 26
# Sample Input 1:
# 8
# Sample Output 1:
# H
# GH
# FGH
# EFGH
# DEFGH
# CDEFGH
# BCDEFGH
# ABCDEFGH
# Sample Input 2:
# 7
# Sample Output 2:
# G
# FG
# EFG
# DEFG
# CDEFG
# BCDEFG
# ABCDEFG


## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while(i<=n):
	j = 1
	start_char = chr(ord("A")+ n-1)
	while(j<=i):
		charp = chr(ord(start_char)-i+j)
		print(charp, end="")
		j = j+1
	print()
	i +=1