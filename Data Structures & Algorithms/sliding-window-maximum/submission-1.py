class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()      # holds INDICES, values decreasing front→back
        res = []

        for r in range(len(nums)):
            # 1. drop indices whose values are smaller than nums[r]
            #    (they can never be the max while nums[r] is around)
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # 2. drop the front if it's slid out of the window
            if dq[0] <= r - k:
                dq.popleft()

            # 3. once the first window is complete, front is the max
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res