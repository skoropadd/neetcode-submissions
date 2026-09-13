class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        prefix = [0] * n
        runner = 0      
        for i in range(n): 
            prefix[i] = runner
            runner = max(runner, height[i])

        postfix = [0] * n
        runner = 0      
        for i in range(n - 1, - 1, - 1): 
            postfix[i] = runner
            runner = max(runner, height[i])

        res = 0 
        for i in range(n): 
            curr = min(prefix[i], postfix[i]) - height[i]
            res += max(0, min(prefix[i], postfix[i]) - height[i])

        return res 