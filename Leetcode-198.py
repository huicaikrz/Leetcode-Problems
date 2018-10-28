# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:39:19 2018

@author: Hui Cai
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for x in nums: 
            last, now = now, max(last + x, now)
        return now
        