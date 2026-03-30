class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # res = []
        # for x in range(2):
        #     for y in nums:
        #         res.append(y)
        # return res

        n = len(nums)
        ans = [0] * (2*n)
        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans