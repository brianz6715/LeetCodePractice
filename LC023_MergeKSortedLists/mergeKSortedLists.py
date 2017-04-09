#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:04:51 2017

@author: BrianzChang
"""
import heapq

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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heap.append((node.val,node))
        heapq.heapify(heap)
        head = ListNode(-1)
        current = head
        while heap:
            pop = heapq.heappop(heap)
            current.next = ListNode(pop[0])
            current = current.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next
        
lists = [ListNode(0),ListNode(3),ListNode(1),ListNode(2)]
heap = []
for node in lists:
    if node:
        heap.append((node.val,node))

for item in heap:
    print item
    
heapq.heapify(heap)

for item in heap:
    print item