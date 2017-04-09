#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 18:32:29 2017

@author: BrianzChang
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        else:
            numRow = len(matrix)
            numCol = len(matrix[0])
            if numRow==0 or numCol==0:
                return False
        
        iRow = numRow-1
        iCol = 0
        
        while True:
            if matrix[iRow][iCol] == target:
                return True
            elif matrix[iRow][iCol] > target:
                iRow -= 1
            elif matrix[iRow][iCol] < target:
                iCol += 1
                
            if iRow < 0 or iCol >= numCol:
                return False

mySolution = Solution()
print mySolution.searchMatrix([[1]], 1)