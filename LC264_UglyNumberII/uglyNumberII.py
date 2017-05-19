#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:49:52 2017

@author: BrianzChang
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        
        while n > 1:
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            minVal = min(u2, u3, u5)
            if minVal == u2:
                i2 += 1
            if minVal == u3:
                i3 += 1
            if minVal == u5:
                i5 += 1
            n -= 1
            ugly.append(minVal)
        return ugly[-1]

mySolution = Solution()
print mySolution.nthUglyNumber(10)