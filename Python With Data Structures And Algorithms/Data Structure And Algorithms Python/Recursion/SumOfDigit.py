# Problem statement
# Write a recursive function that returns the sum of the digits of a given integer.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 12345
# Sample Output 1 :
# 15
# Sample Input 2 :
# 9
# Sample Output 2 :
# 9

## Read input as specified in the question.
## Print output as specified in the question.



def sod(n):
    if len(n) == 1:
        return n[0]
    sum =  sod(n[1:])+n[0] 
    return sum

k = input()
li = [int(i)for i in k]
print(sod(li))
