class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            # adding all values in range [0,n]
            res += (i - nums[i])
        return res
