class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        left, right = 0, len(s) - 1

        while right > left: 
            while right > left and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1

            if s[right] != s[left]: 
                return False
            right -= 1
            left += 1

        return True
        