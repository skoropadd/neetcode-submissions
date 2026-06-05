class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1 # first item to be overwrite 

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
        