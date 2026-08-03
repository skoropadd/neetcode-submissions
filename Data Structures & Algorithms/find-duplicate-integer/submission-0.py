class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0 
        n = len(nums)

        while True: 
            slow = nums[slow]              # one step:  go where slow POINTS
            fast = nums[nums[fast]]        # two steps: follow twice
            if fast == slow: 
                break
        
        slow2 = 0 
        while slow2 != slow: 
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow 