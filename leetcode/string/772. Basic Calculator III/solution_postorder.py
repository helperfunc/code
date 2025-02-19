class Solution:
    def calculate(self, s: str) -> int:
        # tokenize the string to stack, with digits to number
        def tokenize(s):
            i = 0
            res = []
            while i < len(s):
                if s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    res.append(num)
                else:
                    if s[i] in '+-*/()':
                        res.append(s[i])
                        i += 1
                    else:
                        i += 1
            return res
        # tokens = tokenize(s)  "2*(5+5*2)/3" -> [2,*,(,5,+,5,*,2,),/,3]
        # change the inorder expression to postorder expression
        # [2,*,(,5,+,5,*,2,),/,3] -> res = [2,5,5,2,*,+,3,/,*], op = []
        # 6/2+8 => res =[6,2,/,+], [] 
        def inorder_2_postorder(tokens):
            res = []
            ops = []
            # () always add to the ops
            precedence = {'+':1, '-':1, '*': 2, '/': 2, '(': 0, ')': 0}
            for token in tokens:
                if isinstance(token, int):
                    res.append(token)
                elif token == '(':
                    ops.append(token)
                elif token == ')':
                    while ops and ops[-1] != '(':
                        res.append(ops.pop())
                    ops.pop()
                else:
                    while ops and precedence[ops[-1]] >= precedence[token]:
                        res.append(ops.pop())
                    ops.append(token)
            while ops:
                res.append(ops.pop())
            return res
        
        # calculate postorder expression
        def calculate_postorder(tokens):
            res = []
            for token in tokens:
                if isinstance(token, int):
                    res.append(token)
                else:
                    b = res.pop()
                    a = res.pop()
                    if token == '+':
                        res.append(a + b)
                    elif token == '-':
                        res.append(a - b)
                    elif token == '*':
                        res.append(a * b)
                    else:
                        tmp = a // b
                        if tmp >= 0:
                            res.append(tmp)
                        else:
                            res.append(tmp + 1)
            return res[0]

        tokens = tokenize(s)
        tokens = inorder_2_postorder(tokens)
        # print(tokens)
        return calculate_postorder(tokens)
