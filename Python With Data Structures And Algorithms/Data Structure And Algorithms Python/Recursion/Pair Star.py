# Problem statement
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a


## Read input as specified in the question.
## Print output as specified in the question.
def pairstar(str):
    if len(str) == 1:
        return str[0]
    if str[0]==str[1]:
        return str[0]+ "*" + pairstar(str[1:])
    else:
        return str[0] + pairstar(str[1:])     

str = input()
print(pairstar(str))