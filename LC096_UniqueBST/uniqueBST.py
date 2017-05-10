#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:12:39 2017

@author: BrianzChang
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1,1]
        
        for i in range(1,n):
            tmpAns = 0
            for root in range(i+1):
                tmpAns += ans[root] * ans[i-root]
            ans.append(tmpAns)
            
        return ans[n]

mySolution = Solution()
print mySolution.numTrees(3)