class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) + 2
        nums_set = set(nums)

        for i in range(1, n): 
            if i not in nums_set: 
                return i