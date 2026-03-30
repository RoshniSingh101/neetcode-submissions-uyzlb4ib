# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        # call dfs in serialize function
        def dfs(node): # preorder, pass in root
            if not node: # base case
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        # body of serialize function
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",") # splits into array
        self.i = 0 # pointer, want it to be global to access in function dfs inside of deserialize
        def dfs():
            # base case
            if vals[self.i] == "N": 
                self.i += 1 # want to increment i to skip null
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1 # increment to next value
            node.left = dfs()
            node.right = dfs()
            return node # return root node
        return dfs()


