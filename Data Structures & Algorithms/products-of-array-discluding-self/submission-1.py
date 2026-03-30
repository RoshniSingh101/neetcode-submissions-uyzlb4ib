class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        length = len(nums)
        while i < length:
            temp = 1
            for idx, x in enumerate(nums):
                if idx != i:
                    temp *= x
                else:
                    continue
            res.append(temp)
            i += 1
        return res