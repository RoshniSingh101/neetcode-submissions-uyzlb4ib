"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # map old node to clone copy
        oldToNew = {}

        # clone of original node and its neighbors recursively
        def dfs(node):
            # if clone exist, return node
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for n in node.neighbors:
                # add neighbors to copy recursively
                copy.neighbors.append(dfs(n))

            # return clone
            return copy

        # return deep copy of node
        return dfs(node) if node else None

            