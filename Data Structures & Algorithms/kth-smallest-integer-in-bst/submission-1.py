# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 # number of nodes visited
        stack = [] # iterative DFS (in-order traversal)
        cur = root # pointer to keep track of current node

        while cur or stack:
            while cur: 
                # want to go left as much as possible
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() # process most current node
            n += 1
            if n == k: 
                return cur.val # guarenteed to have at least k nodes each time
            cur = cur.right