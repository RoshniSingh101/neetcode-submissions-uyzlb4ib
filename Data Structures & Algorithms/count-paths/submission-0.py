class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n 
        # go thru each row except for the last one
        for i in range(m - 1):
            newRow = [1] * n
            # start at second to last position
            # go right to left
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]