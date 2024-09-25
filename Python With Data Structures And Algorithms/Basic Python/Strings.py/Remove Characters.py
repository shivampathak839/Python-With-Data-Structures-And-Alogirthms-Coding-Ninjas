# Problem statement
# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.

# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# aabccbaa
# a
# Sample Output 1:
# bccb
# Sample Input 2:
# xxyyzxx
# y
# Sample Output 2:
# xxzxx


from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
    n = len(string)
    new =""
    for i in range(n):
        if string[i]==ch:
            continue
        else:
            new = new+string[i]
    return new


#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)

