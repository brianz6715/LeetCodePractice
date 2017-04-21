#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:40:11 2017

@author: BrianzChang
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = [];
        for hr in range(0, 12):
            for mins in range(0, 60):
                if (bin(hr)+bin(mins)).count("1") == num:
                    result.append("%d:%02d"%(hr, mins))
        return result

mySolution = Solution()
print mySolution.readBinaryWatch(4)