class Result:
    def __init__(self):
        self.memo = {}

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        # ((()))   (()())   (())()  ()()()
        # abc -> k1, k2, k3, ... number of parentheses for every part
        # ab  ()()()  a = () b = ()() or a = ()()  b = () duplicates
        # how to divide this problem to smaller problems?
        # multiple ways to divide, restrit the first part of the string to be not dividable
        # a -> not be divided, (a)b
        #  ((())) -> a = (()), b = ""
        #  (()()) -> a = ()(), b = ""
        # (())() -> a = (), b =()
        # ()()() -> a = "", b = ()()
        # if a can be divided to smaller parts, there would be duplicates 
        # (a)b -> key idea
        r = Result()
        if n == 0:
            return [""]
        if n in r.memo:
            return r.memo[n]
        res = []
        for k in range(1, n + 1):
            a = self.generateParenthesis(k - 1)
            b = self.generateParenthesis(n - k)
            for valid_str_a in a:
                for valid_str_b in b:
                    res.append('(' + valid_str_a + ')' + valid_str_b)
        r.memo[n] = res
        return res

