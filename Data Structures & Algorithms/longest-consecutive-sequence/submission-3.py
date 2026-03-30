class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_len = 0
        for x in num_set:
            if x - 1 not in num_set:
                curr_num = x
                curr_len = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(max_len, curr_len)
        return max_len