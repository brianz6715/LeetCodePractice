#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:03:54 2017

@author: BrianzChang
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None
        
    def insert(self, x):
        if self.first == None:
            self.first = ListNode(x)
            self.last = self.first
        elif self.first == self.last:
            self.first.next = ListNode(x)
            self.last = self.first.next
        else:
            current = ListNode(x)
            self.last.next = current
            self.last = self.last.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        type l1: ListNode
        type l2: ListNode
        rtpye: ListNode
        """
        tmp = ListNode(-1)
        head = tmp
        
        while l1 and l2:
            if l1.val > l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
            
        return head.next
    
""" Main """
lst1 = LinkedList()
lst2 = LinkedList()

for i in range(0, 10):
    lst1.insert(i*2)
    lst2.insert(i*2)

mySolution = Solution()
result = mySolution.mergeTwoLists(lst1.first,lst2.first)

tmp = result
while tmp != None:
    print tmp.val
    tmp = tmp.next
    