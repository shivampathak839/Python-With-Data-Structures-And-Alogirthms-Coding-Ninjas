# Problem statement
# Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value of true if it is a palindrome and false if it is not.

# Note: You are not required to print anything, just implement the function. Example:
# Input: s = "racecar"
# Output: true
# Explanation: "racecar" is a palindrome.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# abbba
# Sample Output 1:
# true
# Explanation Of Sample Input 1 :
# “abbba” is a palindrome
# Sample Input 2:
# abcd
# Sample Output 2:
# false
# Explanation Of Sample Input 2 :
# “abcd” is not a palindrome.
# Constraints:
# 0 <= |S| <= 10^6
# where |S| represents the length of string S.

## Read input as specified in the question.
## Print output as specified in the question.


from tabnanny import check


def checkp(string):
    if len(string)==1:
        

        return string[0]
        
        
    output = checkp(string[1:])
    new = output + string[0]
    return new



    

n = input()
check = checkp(n)  
if check == n:
    print("true")
else:
    print("false")

    

        