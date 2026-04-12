class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case if nums has one element nums[0]
        # skip first house, skip last house
        # get max of both house
        return max(nums[0], 
            self.helper(nums[1:]), 
            self.helper(nums[:-1]))

    def helper(self, nums):
        r1, r2 = 0, 0
        for n in nums:
            # get max of current house + rob1 and rob2
            # n is adj to rob2, therefore skip it
            maxR = max(r1 + n, r2)
            r1 = r2 # update r1 to next (r2)
            r2 = maxR # update to max
        return r2
        