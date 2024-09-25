# Problem statement
# For a given a string(str), find and return the highest occurring character.

# Example:
# Input String: "abcdeapapqarr"
# Expected Output: 'a'
# Since 'a' has appeared four times in the string which happens to be the highest frequency character, the answer would be 'a'.
# If there are two characters in the input string with the same frequency, return the character which comes first.

# Consider:
# Assume all the characters in the given string to be in lowercase always.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 0 <= N <= 10^6
# Where N is the length of the input string.

# Time Limit: 1 second
# Sample Input 1:
# abdefgbabfba
# Sample Output 1:
# b
# Sample Input 2:
# xy
# Sample Output 2:
# x


from sys import stdin


def highestOccuringChar(string) :

	#Your code goes here
    ascii_size = 256
    ctr = [0]*256
    max = -1
    ch =""
    for i in string:
        ctr[ord(i)] +=1
    for i in string:
        if max<ctr[ord(i)]:
            max = ctr[ord(i)]
            ch = i
    return ch            
    

#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)


