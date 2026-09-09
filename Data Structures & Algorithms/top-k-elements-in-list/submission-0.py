class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dct = {}

        for num in nums:
            if num in dct:
                dct[num] += 1 
            else:
                dct[num] = 1

        res = []

        for num, cnt in dct.items():
            heapq.heappush(res, (cnt, num))
            if len(res) > k:
                heapq.heappop(res)

        return [num for _, num in res]