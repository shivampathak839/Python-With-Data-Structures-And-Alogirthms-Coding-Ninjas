# Problem statement
# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 < |S| <= 9
# where |S| represents length of string S.
# Sample Input 1 :
# 00001231
# Sample Output 1 :
# 1231
# Sample Input 2 :
# 12567
# Sample Output 2 :
# 12567


## Read input as specified in the question.
## Print output as specified in the question.
def stringToInt(str):
 
    # If the number represented as a string
    # contains only a single digit
    # then returns its value
    if (len(str) == 1):
        return ord(str[0]) - ord('0')
 
    # Recursive call for the sub-string
    # starting at the second character
    y = stringToInt(str[1:])
 
    # First digit of the number
    x = ord(str[0]) - ord('0')
 
    # First digit multiplied by the
    # appropriate power of 10 and then
    # add the recursive result
    # For example, xy = ((x * 10) + y)
    ans = x * (10**(len(str) - 1)) + y
    return ans
 
 
# Driver code
str = input()
print(stringToInt(str))