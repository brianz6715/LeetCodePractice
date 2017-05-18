#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:41:42 2017

@author: BrianzChang
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        for fac in 2,3,5:
            while num % fac == 0:
                num /= fac
        return num == 1
    
mySolution = Solution()
print mySolution.isUgly(16)