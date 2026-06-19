class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        res = [0] * k
        max_diff = float("inf")
        window_sum = 0  # the window's running state

        for r in range(len(arr)):
            window_sum += abs(arr[r] - x)

            if r >= k:
                window_sum -= abs(arr[r - k] - x)

            if r >= k - 1 and window_sum < max_diff:
                max_diff = window_sum
                res[:] = arr[r - k + 1 : r + 1]

        return res
