class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True


        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        
        return True
