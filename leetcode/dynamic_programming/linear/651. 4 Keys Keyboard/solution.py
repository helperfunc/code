class Solution:
    def maxA(self, n: int) -> int:
        if n < 4:
            return n

        length = [0] * (n + 1)
        for i in range(4):
            length[i] = i
        
        for i in range(4, n + 1):
            length[i] = length[i - 1] + 1 # the ith pos is A
            for k in range(1, i):
                length[i] = max(length[i], length[k] * (i - k -1))
        
        return length[n]