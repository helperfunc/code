class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # n -> (n-1)//2  n=3->1 -> [10**1, 10**2)+reverse=palindrome, n=2->0 -> [10**0, 10**1)
        # sorted() -> get the representative of the palindrome 
        # for the representative, (n-count[0])*(n-1)!
        # 23532 -> (n-count[0])*(n-1)! / prod((count[i])!) number of palindromes for the representative
        fac = [factorial(i) for i in range(n+1)] # count can be n
        res = 0
        base = 10**((n-1)//2)
        v = set()
        for val in range(base, base*10):
            s = str(val)
            s += s[::-1][n%2:] #235 32  s is a palindrome
            if int(s) % k:
                continue
            s_rep = ''.join(sorted(s)) # representative of the palindrome
            if s_rep in v:
                continue
            v.add(s_rep)
            count = Counter(s_rep)
            tmp = (n - count['0'])*fac[n-1]
            tmpprod = 1
            for i in range(10):
                if count[str(i)] != 0:
                    tmpprod *= fac[count[str(i)]]
            tmp //= tmpprod
            res += tmp
        return res
