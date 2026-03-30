# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if we have an empty root, return None
        if not root: return None

        # swap the children each time
        tmp = root.left # store left (can be right) into a variable
        root.left = root.right # make the left node the right node
        root.right = tmp # store left into right

        self.invertTree(root.left) # DFS, keep exploring children of left until all are visited
        self.invertTree(root.right) # when finished, DFS keep exploring children of left until all are visited
        return root # return root when finished visiting and exploring all nodes