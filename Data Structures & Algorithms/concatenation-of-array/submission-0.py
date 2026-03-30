class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for x in range(2):
            for y in nums:
                res.append(y)
        return res