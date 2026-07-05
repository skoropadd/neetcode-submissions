class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = 0 
        counts = {}
        res = ""
        min_length = float('inf')
        required = Counter(t)

        for r in range(len(s)): 
            counts[s[r]] = counts.get(s[r], 0) + 1
            while all(counts.get(ch, 0) >= need for ch, need in required.items()):
                if r + 1 - l < min_length: 
                    res = s[l : r + 1]
                    min_length = r + 1 - l 
                counts[s[l]] = counts.get(s[l], 0) - 1
                l += 1

        return res