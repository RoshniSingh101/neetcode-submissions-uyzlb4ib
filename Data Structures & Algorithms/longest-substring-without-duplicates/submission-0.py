class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in set_s:
                set_s.remove(s[l])
                l += 1
            set_s.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len