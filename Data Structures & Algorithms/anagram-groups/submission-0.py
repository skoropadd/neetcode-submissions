class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dct = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            dct[key].append(s)

        return list(dct.values())