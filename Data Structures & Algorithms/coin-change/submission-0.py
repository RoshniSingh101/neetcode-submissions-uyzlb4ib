class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ensure max is in each element of array
        # can use infinity, but amount + 1 is max
        # ex amount 7 -> 8 for each element
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # compute a amount
        for a in range(1, amount + 1):
            for c in coins:
                # ensures solution is positive
                if a - c >= 0:
                    # 1 comes from current coin
                    # does not mean coin of value 1
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # edge case
        return dp[amount] if dp[amount] != amount + 1 else -1