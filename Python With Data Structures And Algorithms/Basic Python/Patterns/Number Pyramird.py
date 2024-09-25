# Problem statement
# Print the following pattern for a given n.

# For eg. N = 6
# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456
# Sample Input 1 :
# 4
# Sample Output 1 :
# 1234
#   234
#     34
#       4
#     34
#   234
# 1234
## Read input as specified in the question.
## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.
num = int(input())
i =0
while(num>i):
    space = 1
    while(space<=i):
        print(" ",end="")
        space +=1
    j=1
    while num-i>=j:
        print(j+i,end="")
        j+=1
    i+=1
    print()
while i>1:
    space = 1
    while space<=i-2:
        print(" ",end="")
        space=space+1
    j=num
    k=1
    while j>=i-1:
        print(i+k-2, end="")
        j-=1
        k+=1
    i-=1
    print()

