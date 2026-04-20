class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # time complexity O (m * n)
        # space complexity O(1) b/c do not count output as extra memory
        res = []
        left, right = 0, len(matrix[0]) # right is num of columns
        top, bottom = 0, len(matrix) # bottom is num of rows

        while left < right and top < bottom:
            # left to right and get every i in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1]) # right is out of bounds
            right -= 1

            # edge case if only have one col or one row
            if not (left < right and top < bottom):
                break

            # get every i in bottom row (reverse order)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i]) # bottom is out of bounds
            bottom -= 1

            # every i in left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

