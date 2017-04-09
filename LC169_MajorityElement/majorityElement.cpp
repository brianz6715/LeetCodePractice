/*
 * majorityElement.cpp
 *
 *  Created on: 2017年4月9日
 *      Author: BrianzChang
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
    	int len = nums.size();
    	if (len == 1)
    		return nums[0];

    	int candidate = 0;
    	int cnt = 0;
    	for (int i=0; i<len; i++) {
    		if ((candidate != nums[i]) && (cnt == 0))
    			candidate = nums[i];
    		else if (candidate != nums[i])
    			cnt -= 1;
    		else if (candidate == nums[i])
    			cnt += 1;
    	}
    	return candidate;
    }
};

int main() {
	// Generate testing data
	int arr[] = {0, 0, 1, 2, 0, 3, 0, 4, 0, 0};
	vector<int> nums(arr, arr + sizeof(arr)/sizeof(arr[0]));

	// Process
	Solution mySolution;
	int answer = mySolution.majorityElement(nums);
	// Print
	for (vector<int>::iterator it=nums.begin(); it!=nums.end(); ++it){
		cout << *it << "\t";
	}
	cout << endl << answer << endl;

	return 0;
}

