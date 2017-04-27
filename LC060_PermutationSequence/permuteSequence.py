#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 00:57:01 2017

@author: BrianzChang
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        f = 1
        candidate = ''
        for i in range(1,n+1):
            f *= i
            candidate += str(i)
        
        print candidate
        s = ''
        tmpRes = k-1
        for j in range(n,0,-1):
            f /= j
            if tmpRes == 0:
                ans = 0
            else:
                ans = tmpRes/f
            s += candidate[ans]
            tmpRes %= f
            candidate = candidate.replace(candidate[ans],'')
            print candidate
        
        return s

mySolution = Solution()
print mySolution.getPermutation(4,12)
