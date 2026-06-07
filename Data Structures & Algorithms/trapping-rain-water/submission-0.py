class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        prefix = [0] * n 
        runner = 0
        for i in range(n): 
            runner = max(runner, height[i])
            prefix[i] = runner 
        print(prefix) 

        postfix = [0] * n 
        runner = 0 
        for i in range(n - 1, - 1, - 1):
            runner = max(runner, height[i])
            postfix[i] = runner
        print(postfix) 

        res = 0 
        for i in range(n):
            res += min(prefix[i], postfix[i]) - height[i]
        return res 


