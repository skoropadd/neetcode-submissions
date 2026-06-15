class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        for i in range(len(strs[0])): 
            curr = set()
            for s in strs: 
                if i >= len(s): 
                    return res
                else: 
                    curr.add(s[i])

            if len(curr) == 1: 
                res += strs[0][i]
            else: 
                return res
        return res