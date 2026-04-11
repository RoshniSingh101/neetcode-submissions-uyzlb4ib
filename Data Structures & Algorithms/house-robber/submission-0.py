class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        # [r1, r2, n, n+1, ...]
        # cannot rob adjacent houses
        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp # think fibonnaci sequence
        return r2