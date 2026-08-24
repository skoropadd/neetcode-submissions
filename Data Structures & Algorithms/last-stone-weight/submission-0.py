class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            delta = abs(a - b)
            if delta != 0: 
                heapq.heappush(stones, -delta)
        
        return -stones[0] if stones else 0