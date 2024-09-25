# Problem statement
# Given a string S, remove consecutive duplicates from it recursively.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string
# Sample Input 1 :
# aabccba
# Sample Output 1 :
# abcba
# Sample Input 2 :
# xxxyyyzwwzzz
# Sample Output 2 :
# xyzwz


# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)== 0 or len(string)==1:
        return string
    if string[0]!=string[1]:
        return string[0]+removeConsecutiveDuplicates(string[1:])
    else:    
        return removeConsecutiveDuplicates(string[1:])

                  
    

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
