# Problem statement
# Print the following pattern for the given N number of rows.

# Pattern for N = 4
# 1234
# 123
# 12
# 1
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input :
# 5
# Sample Output :
# 12345
# 1234
# 123
# 12
# 1

n = int(input())
i = 1
p = n
while(i<=n):
	j = 1
	while(j<=p):
		print(j, end="")
		j=j+1
	print()
	i = i+1
	p=p-1