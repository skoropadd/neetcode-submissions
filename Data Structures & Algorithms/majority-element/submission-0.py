class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) / 2
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        res = [k for k, v in counter.items() if v >= target]

        return res[0]