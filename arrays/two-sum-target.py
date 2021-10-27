'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


# we will be creating a complimentary list that will contain the substraction of the target number and
# the number being evaluated. That way, if the next evaluated number is inside that list, that's the solution
class Solution:
    def twoSum(nums, target):
        complementary = []
        for idx, elem in enumerate(nums):
            if elem in complementary:
                return [complementary.index(elem), idx]
            else:
                complementary.append(target-elem)


if __name__ == '__main__':
    print(Solution.twoSum([2, 7, 11, 15], 9))
    print(Solution.twoSum([3, 2, 4], 6))
    print(Solution.twoSum([3, 3], 6))
