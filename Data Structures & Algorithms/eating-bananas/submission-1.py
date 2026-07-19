class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles) + 1

        while l <= r: 
            k = (l + r) // 2
            curr_h = 0 

            for pile in piles: 
                curr_h += -(-pile // k)

            if curr_h <= h:      # works (fast enough) → try slower
                r = k - 1
            else:                # too slow → go faster
                l = k + 1
        return l             # first "yes" — your card's invariant

