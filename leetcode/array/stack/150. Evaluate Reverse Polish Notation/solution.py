class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # a b op
        # save the value to the stack and while encounter operators, pop the value
        # 1 + 1 => 1 1 +
        n = len(tokens)
        stack = []
        for i in range(n):
            if tokens[i] in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.cal(a, b, tokens[i]))
            else:
                stack.append(int(tokens[i]))
                
        return stack[-1]
    
    def cal(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            tmp = a // b
            if tmp < 0 and a % b != 0:
                tmp += 1
            return tmp
    

