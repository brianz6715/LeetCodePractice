#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:22:58 2017

@author: BrianzChang
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ Moore voting algorithm"""
        
        # 82 ms
        candidate = 0
        cnt = 0
        for item in nums:
            if item != candidate and cnt == 0:
                candidate = item
                cnt = 1
            elif item != candidate:
                cnt -= 1
            elif item == candidate:
                cnt += 1
            else:
                print "There must be sth wrong"
        return candidate
        """
        # 88ms, 66ms, 52ms
        candidate, cnt = 0, 0
        for item in nums:
            if item == candidate:
                cnt += 1
            elif cnt == 0:
                candidate, cnt = item, 1
            else:
                cnt -= 1
        return candidate
        “”“

mySolution = Solution()
list_test = [0, 3, 4, 0, 0, 0, 0, 0, 3, 7, 8];
print mySolution.majorityElement(list_test)