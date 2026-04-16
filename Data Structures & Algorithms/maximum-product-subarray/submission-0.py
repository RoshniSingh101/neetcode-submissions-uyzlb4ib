class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # negative values can exist therefore do not use 0
        curMin, curMax = 1, 1

        for n in nums:
            # not necessary, but still works
            if n == 0:
                curMin, curMax = 1, 1
                continue
            # have temp variable so that curMin doesn't mix up calculations
            tmp = curMax * n
            # cache max, min, and n itself
            # for curMax and curMin
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            res = max(curMin, curMax, res)
        
        return res