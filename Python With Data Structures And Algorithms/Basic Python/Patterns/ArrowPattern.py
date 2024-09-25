# Problem statement
# Print the following pattern for the given number of rows.

# Assume N is always odd.

# Note : There is space after every star. Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input :
# 11
# Sample Output :
# *
#  * *
#    * * *
#      * * * *
#        * * * * *
#          * * * * * *
#        * * * * *
#      * * * *
#    * * *
#  * *
# *


## Read input as specified in the question.
## Print output as specified in the question.
n =int(input())
n1 = (n+1)//2
n2= n//2

for i in range(1,n1+1):
   for s in range(0,i-1):
      print(" ", end="")
   for j in range(i):
      print("* ", end="")
   print()

for i in range(1,n2+1):
   for s in range(1,n2-i+1):
      print(" ", end="")
   for j in range(n2-i+1):
      print("* ", end="")
   print()