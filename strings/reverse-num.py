'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-2^31 <= x <= 2^31 - 1
'''


class Solution:
    def reverse(x):
        if x == 0:
            return 0
        neg = 0
        if x < 0:
            x = abs(x)
            neg = 1
        rev = int(str(x)[::-1])
        if rev > (pow(2, 31)-1) or rev < -(pow(2, 31)):
            return 0
        if neg == 1:
            rev = -rev
        return rev


if __name__ == '__main__':
    print(Solution.reverse(230))
    print(Solution.reverse(-230))
    print(Solution.reverse(0))
