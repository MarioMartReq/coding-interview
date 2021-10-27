'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
'''

# count zeros, remove all zeros, place those zeroes in the back.


class Solution:
    def moveZeroes(nums):
        num_zeroes = nums.count(0)
        nums[:] = list(filter(lambda val: val != 0, nums))
        for i in range(num_zeroes):
            nums.append(0)
        return nums


if __name__ == '__main__':
    print(Solution.moveZeroes([0, 1, 0, 3, 12]))
    print(Solution.moveZeroes([0]))
