# Problem statement
# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.

# Permutations of each other
# Two strings are said to be a permutation of each other when either of the string's characters can be rearranged so that it becomes identical to the other one.

# Example: 
# str1= "sinrtg" 
# str2 = "string"

# The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings are a permutation of each other.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# abcde
# baedc
# Sample Output 1:
# true
# Sample Input 2:
# abc
# cbd
# Sample Output 2:
# false


from stat import FILE_ATTRIBUTE_SPARSE_FILE
import string
from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    ctr1 = [0]*256
    ctr2 = [0] * 256
    for i in string1:
        ctr1[ord(i)] +=1
    for j in string2:
        ctr2[ord(j)] +=1
    if ctr1 == ctr2:
        return True
    else:
        return False            



#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

