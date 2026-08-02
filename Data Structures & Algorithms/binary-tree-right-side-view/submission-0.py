# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        queue = deque()
        if root: 
            queue.append(root)

        while queue: 
            n = len(queue)
            curr_level_values = []
            for _ in range(n): 
                curr = queue.popleft()
                curr_level_values.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            most_right = curr_level_values[-1]
            res.append(most_right)
        return res 