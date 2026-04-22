class Solution:
    def hammingWeight(self, n: int) -> int:
        # more efficient solution
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res

        # res = 0
        # while n: # while n is >= 0
        #     res += n % 2
        #     n = n >> 1 # bit shift to right by 1
        # return res

        # # time complexity
        # # O(32) or O(1) b/c each input is 32 bits

        # # memory complexity 
        # # O(1)
