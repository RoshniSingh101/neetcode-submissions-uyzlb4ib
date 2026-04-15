class Solution:
    def numDecodings(self, s: str) -> int:
        # recursive
        dp = { len(s) : 1 }

        def dfs(i):
            # base case
            # i in cache
            # or reached end of string
            if i in dp:
                return dp[i]
            # if not at end, bad base case
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            # check if index in bounds
            # if starts with a 1, num can be 10-19
            # if starts with a 2, num can be 20-26
            if i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i+1] in "0123456"):
                res += dfs(i + 2) # for double digit values
            dp[i] = res # cache
            return res
        return dfs(0)