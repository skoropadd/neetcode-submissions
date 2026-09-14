class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        curr = 1
        for i in range(len(nums)): 
            curr *= nums[i]
            prefix.append(curr)

        postfix = []
        curr = 1
        for i in range(len(nums) - 1, - 1, - 1):
            curr *= nums[i]
            postfix.append(curr)
        postfix.reverse()
        postfix.append(1)

        answer = []
        for i in range(len(nums)): 
            answer.append(prefix[i] * postfix[i + 1])

        return answer 