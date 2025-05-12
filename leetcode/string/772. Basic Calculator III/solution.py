class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        val = 0
        tokens = []
        ops = [] # as a stack to get the order of the operators and added these ops to the tokens
        tokened_val = True
        needs_zeros = True
        for i in range(n):
            if s[i].isdigit():
                val = val * 10 + ord(s[i]) - ord('0')
                tokened_val = False
                continue
            elif tokened_val == False:
                tokens.append(str(val))
                tokened_val = True
                val = 0
                needs_zeros = False

            if s[i] == ' ': continue

            # ()
            if s[i] == '(':
                ops.append(s[i])
                needs_zeros = True
                continue
            if s[i] == ')':
                while ops and ops[-1] != '(': #tokens would contains the values in the brackets
                    tokens.append(ops.pop())
                ops.pop()
                needs_zeros = False
                continue
            
            if needs_zeros: tokens.append("0")
            # operators
            # 3*2+2
            # tokens = ["3", "2",]
            # ops = ["*"] # op should be calculated before the current op, added it to the tokens
            while ops and self.getRank(ops[-1]) >= self.getRank(s[i]):
                tokens.append(ops.pop())
            ops.append(s[i])

        if tokened_val == False:
            tokens.append(str(val))
        while ops:
            tokens.append(ops.pop())

        print(tokens)
        return self.evalRPN(tokens)

    def getRank(self, op):
        if op == '+' or op == '-': return 1
        if op == '*' or op == '/': return 2
        return 0 # (


            
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
    

