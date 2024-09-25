# Problem statement
# Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 <= M <= 1000
# 0 <= N <= 1000
# Sample Input 1 :
# 3 
# 5
# Sample Output 1 :
# 15
# Sample Input 2 :
# 4 
# 0
# Sample Output 2 :
# 0


def product( x , y ):
    # if x is less than y swap
    # the numbers
    if x < y:
        return product(y, x)
     
    # iteratively calculate y
    # times sum of x
    elif y != 0:
        return (x + product(x, y - 1))
     
    # if any of the two numbers is
    # zero return zero
    else:
        return 0
 
# Driver code
x = int(input())
y = int(input())
print( product(x, y))