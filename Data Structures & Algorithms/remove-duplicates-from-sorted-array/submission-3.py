class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        slow = 0
        for fast in range(len(nums)):
            if slow < k or nums[fast] != nums[slow - k]:
                nums[slow] = nums[fast]
                slow += 1
        return slow