class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:            # strict — stop when they MEET
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1     # min is strictly right of mid (mid can't be it)
            else:
                r = mid         # min is at mid or left — keep mid
        return nums[l]          # l == r → they converged ON the minimum

