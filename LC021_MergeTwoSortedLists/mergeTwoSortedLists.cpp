/*
 * mergeTwoSortedLists.cpp
 *
 *  Created on: 2017年4月9日
 *      Author: BrianzChang
 */


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <iostream>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    	ListNode tmp = ListNode(0);
    	ListNode *tail = &tmp;
    	while (l1 && l2) {
    		if (l1->val < l2->val) {
    			tail->next = l1;
    			l1 = l1->next;
    		}
    		else {
    			tail->next = l2;
    			l2 = l2->next;
    		}
    		tail = tail->next;
    	}
    	return tmp.next;
    }
};

int main() {
	// Generate 2 lists
	ListNode l1 = ListNode(0);
	ListNode l2 = ListNode(0);
	ListNode *tailL1 = &l1;
	ListNode *tailL2 = &l2;
	for (int i=0; i < 10; i++) {
		int rand_l1 = i*2;//std::rand();
		int rand_l2 = i*2+1;//std::rand();
		tailL1->next = new ListNode(rand_l1);
		tailL2->next = new ListNode(rand_l2);
		tailL1 = tailL1->next;
		tailL2 = tailL2->next;
		cout << rand_l1 <<"\t"<< rand_l2 <<endl;
	}
	// Call solution
	Solution mySolution;
	ListNode *result =  mySolution.mergeTwoLists(l1.next, l2.next);
	// Print
	while (result) {
		cout << result->val << "\t";
		result = result->next;
	}

	return 0;
}

