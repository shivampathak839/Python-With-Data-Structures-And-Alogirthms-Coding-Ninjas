# Problem statement
# For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest sum(sum of all the elements in a row or column) amongst all the rows/columns.

# Note :
# If there are more than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= t <= 10^2
# 1 <= N <= 10^3
# 1 <= M <= 10^3
# Time Limit: 1sec
# Sample Input 1:
# 1
# 3 2
# 6 9 
# 8 5 
# 9 2 
# Sample Output 1:
# column 0 23
# Sample Input 2:
# 1
# 4 4
# 6 9 8 5 
# 9 2 4 1 
# 8 3 9 3 
# 8 7 8 6 
# Sample Output 2:
# column 0 31


'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    row_index = 0
    col_index = 0
    
    row_sum = 0
    col_sum = 0
    if nRows == 0 and mCols ==0:
        print("row "+str(0)+" "+str(-2147483648))
        exit()
    for i in range(nRows):
        rowsum = 0
        for j in range(mCols):
            
            rowsum += arr[i][j]
            
        if rowsum> row_sum:
            
            row_sum = rowsum
            row_index = i
    for j in range(mCols):
        colsum = 0
        for i in range(nRows):
            colsum += arr[i][j]
        if colsum > col_sum:
            col_sum = colsum
            col_index = j

    

    if row_sum >= col_sum:
        print("row "+str(row_index)+" "+str(row_sum))
    else:
        print("column "+str(col_index)+" "+str(col_sum))


        
    





























#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1