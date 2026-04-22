class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n: # while n is >= 0
            res += n % 2
            n = n >> 1 # bit shift to right by 1
        return res
