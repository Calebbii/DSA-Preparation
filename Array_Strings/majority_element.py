""" Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space? """

def majorityElement(nums):
    for n in range(len(nums)):
        count =0
        for x in range(len(nums)):
            if nums[x]==nums[n]:
                count+=1
        if count>len(nums)/2:
            return nums[n]
        
test2 = [2,2,1,1,1,2,2]
print(majorityElement(test2))
