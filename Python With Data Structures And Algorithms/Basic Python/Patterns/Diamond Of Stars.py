# Problem statement
# Print the following pattern for the given number of rows.

# Note: N is always odd.


# Pattern for N = 5



# The dots represent spaces.




# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= N <= 49
# Sample Input 1:
# 5
# Sample Output 1:
#   *
#  ***
# *****
#  ***
#   *
# Sample Input 2:
# 3
# Sample Output 2:
#   *
#  ***
#   *

n = int(input())
n1= int((n+1)/2)
n2 = n//2
for i in range(1,n1+1):
    for s in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i-1+1):
        print("*", end="")
    print()
for i in range(n2,0,-1):
    for s in range(1,n2-i+1+1):
        print(" ",end="")
    for j in range( 1,2*i-1+1):
        print("*", end="")
    print()



