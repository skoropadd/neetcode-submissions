class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]: 
            return True 

        for i in range(len(s)): 
            new_s = s[:i] + s[i + 1:]
            if new_s == new_s[::-1]:
                return True

        return False
            
