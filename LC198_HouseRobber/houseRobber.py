#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: BrianzChang
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums
        elif length == 2:
            return max(nums)
        
        for i in range(length):
            