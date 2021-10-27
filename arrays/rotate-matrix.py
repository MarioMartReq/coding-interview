'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''


# Explanation: to rotate a matrix, you can reverse it and then transpose it
# This procedure does exactly that.
# matrix[::-1] reverses the matrix
# then, the * separates the column list into a different argument
# then, the zip takes the first (then the second, third...) element from each list and makes it list
class Solution:
    def rotate(matrix):
        matrix[::] = list(zip(*matrix[::-1]))


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution.rotate(matrix)
    print(matrix)
