# Problem statement
# Given a string, compute recursively a new string where all 'x' chars have been removed.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string S. 
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# Sample Input 2 :
# abc
# Sample Output 2:
# abc

# Problem: Remove x from string
from os import remove


def removeX(string): 
    if len(string) ==0:
        return string
    newoutput = removeX(string[1:])
    if string[0] == "x":
        return newoutput
    else:
        return string[0]+ newoutput       

# Main
string = input()
print(removeX(string))

