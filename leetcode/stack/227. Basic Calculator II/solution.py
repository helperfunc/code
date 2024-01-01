class Solution:
    def calculate(self, s: str) -> int:
        # " 3-5 / 2 "
        # prev_op is the op [*, /] to cal prev_val in the stack and the cur_val,
        # add the result to the stack
        # if prev_op == '-', save negative value to the stack
        n = len(s)
        res = 0
        i = 0
        prev_op = '+'
        tmpv = 0
        stack = []
        while i < n:
            # if s[i] == ' ': # because the last charater of the string can be ' '
            #     i += 1
            if s[i].isdigit():
                tmpv = tmpv * 10 + int(s[i])
            if i == n - 1 or (i < n and s[i] in ['+', '-', '*', '/']):
                if prev_op == '+':
                    stack.append(tmpv)
                elif prev_op == '-':
                    stack.append(-tmpv)
                elif prev_op == '*':
                    stack.append(tmpv * stack.pop())
                else:
                    v = stack.pop()
                    tmpr = v // tmpv
                    if tmpr < 0 and v % tmpv != 0:
                        tmpr += 1
                    stack.append(tmpr)

                prev_op = s[i]
                
                tmpv = 0
            i += 1
        return sum(stack)
