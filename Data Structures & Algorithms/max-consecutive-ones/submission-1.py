class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        abs_max = 0
        curr_max = 0 

        for num in nums: 
            if num == 1:
                curr_max += 1
                abs_max = max(abs_max, curr_max)
            else: 
                curr_max = 0 
        return abs_max
        