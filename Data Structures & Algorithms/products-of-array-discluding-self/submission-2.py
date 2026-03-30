class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        length = len(nums)
        while i < length:
            temp = 1
            for index, value in enumerate(nums): # fixed to compare indicies instead of values
                if index != i:
                    temp *= value
            res.append(temp)
            i += 1
        return res