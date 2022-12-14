# -*- coding: utf-8 -*-
"""HW2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MNBDfr_oQGwbLbcR24FXZ8MnINvzN5SE
"""

# CS 3190 - HW2
# Jessika Jimenez

from math import sqrt
row = 3
col = 3
 
# Function to return the Frobenius
# Norm of the given matrix
def frobeniusNorm(mat):
 
    # To store the sum of squares of the
    # elements of the given matrix
    sumSq = 0
    for i in range(row):
        for j in range(col):
            sumSq += pow(mat[i][j], 2)
 
    # Return the square root of
    # the sum of squares
    res = sqrt(sumSq)
    return round(res, 5)
 
mat = [ [ 0,2,0 ], [ -1,0,0 ], [ 0,0,4 ] ]
print(frobeniusNorm(mat))
 
# This code is contributed by mohit kumar 29
# Altered by Jessika Jimenez