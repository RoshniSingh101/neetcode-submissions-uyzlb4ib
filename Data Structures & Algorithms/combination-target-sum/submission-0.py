class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base case for success
            if total == target: 
                res.append(cur.copy())
                return
            # if not successful
            if i >= len(nums) or total > target: return

            # first decision to include nums
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # second decision to not include nums (don't add values)
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res