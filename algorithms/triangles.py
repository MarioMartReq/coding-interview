'''
https://app.codility.com/demo/results/trainingDQWMT8-J9G/
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''

# P < Q < R
# there are three total conditions:
# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# but if we order the array, we know that A[R]+A[Q] are ALWAYS going to be bigger than A[P]
# and A[P]+A[R] are ALWAYS going to be bigger than A[Q], so the only condition to check is
# A[P]+A[Q] > A[R], and when this condition is met, we return 1. Otherwise, 0

'''Complexity: O(n log(n)) due to the sort'''


def solution(A):
    length = len(A)
    if length < 3:
        return 0
    A.sort()
    for i in range(0, length-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    return 0


def test():
    A = [10, 2, 5, 1, 8, 20]
    B = [10, 50, 5, 1]
    expectedA = 1
    expectedB = 0
    print("expected A: " + str(expectedA))
    print("obtained A: " + str(solution(A)))
    print("expected B: " + str(expectedB))
    print("obtained B: " + str(solution(B)))


if __name__ == '__main__':
    test()
