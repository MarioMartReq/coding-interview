'''
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106'''

# this algorithm implements the sieve of erastosthenes
# good explanation: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# this algorithm obtains all prime numbers under N in (n log(log(n))) time


class Solution:
    def countPrimes(n):

        prime = [True for i in range(n+1)]
        p = 2
        # we only need to explore till sqrt of N
        # the prime numbers will be the ones with True
        while(p*p <= n):
            # if a number is a prime (True), we know that from that point, all of its multiples are not prime
            # so we mark as false for the rest of the multiples up to the number we are looking
            # only the numbers that previously didn't have a divisor will remain as primes
            if prime[p] == True:
                # start, stop, step
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1

        # we transform the Trues into a list of primes
        result = [i for i in range(2, n+1) if prime[i] == True]
        print(result)
        # result contains a list of primes up to the n number.
        return len(result)


if __name__ == '__main__':
    print(Solution.countPrimes(50))
