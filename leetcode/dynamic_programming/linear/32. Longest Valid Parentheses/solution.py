class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        length = [0] * n
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                continue
            if i - 1 > -1 and s[i - 1] == '(':
                length[i] = length[i - 2] + 2
            elif i - 1 > -1 and s[i - 1] == ')':
                if i - length[i - 1] - 1 > -1 and s[i - length[i - 1] - 1] == '(':
                    length[i] = length[i - 1] + 2
                    if i - length[i - 1] - 2 > -1:
                        length[i] += length[i - length[i - 1] - 2]
            res = max(res, length[i])
        
        return res