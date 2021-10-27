'''
Simple problem: is N a power of M? 
'''


class Solution:
    def isPowerOfM(m, n):
        if n <= 0:
            return False
        # for example, 9 and 27 are powers of 3 and they both are divisors of 81, 243.
        # We simply take a big enough number, and if it is divisible by the asked number, okey
        maxim = pow(m, 19)
        return maxim % n == 0


if __name__ == '__main__':
    print(Solution.isPowerOfM(3, 81))
    print(Solution.isPowerOfM(2, 81))
