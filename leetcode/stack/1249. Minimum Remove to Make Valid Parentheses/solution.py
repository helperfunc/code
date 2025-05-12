class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        n = len(s)
        left_bracket, right_bracket = 0, 0
        for c in s:
            if c == '(':
                left_bracket += 1
                stack.append(c)
            elif c == ')':
                if left_bracket > 0:
                    left_bracket -= 1
                    stack.append(c)
            else:
                stack.append(c)
        stack1 = []
        for i in range(len(stack) - 1, -1, -1):
            c = stack[i]
            if c == ')':
                right_bracket += 1
                stack1.append(c)
            elif c == '(':
                if right_bracket > 0:
                    stack1.append(c)
                    right_bracket -= 1
            else:
                stack1.append(c)
        
        res = []
        for i in range(len(stack1)):
            res.append(stack1.pop())
        
        return ''.join(res)