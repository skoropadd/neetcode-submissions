# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.res = 0 
        max_so_far = float('-inf')

        def dfs(node, max_so_far): 
            if not node: 
                return 
            if node.val >= max_so_far: 
                self.res += 1 
            new_max = max(max_so_far, node.val)
            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, max_so_far)
        return self.res 
        