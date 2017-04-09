#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 00:15:42 2017

@author: BrianzChang
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 122 ms
        return self.subMajority(nums, 0, len(nums))
        
    def subMajority(self, nums, first, last):
        if first == last-1:
            return nums[first]
        
        mid = (first + last)/2
        leftM = self.subMajority(nums,first,mid)
        rightM = self.subMajority(nums,mid,last)
        
        if leftM == rightM:
            return leftM
        
        if nums[first:last].count(leftM) > nums[first:last].count(rightM):
            return leftM
        else:
            return rightM

mySolution = Solution()
list_test = [0, 3, 4, 0, 3, 3, 3, 0, 3, 7, 3];
print mySolution.majorityElement(list_test)