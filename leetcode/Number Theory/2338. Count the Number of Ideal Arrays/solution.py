MOD = 1000000007
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # arr_a = [a0, a1, a2, ..., an]
        # arr_b = [a0, a1/a0, a2/a1,...,an/a(n-1)]
        # arr_a <=> arr_b <=> product arr_b product(a0,a1/a0, a2/a1,...,an/a(n-1)) = an
        # value = product(prime_i^e) = an
        # [][][][][] n=5, a_n = 8, prime = 2, e=3
        # [][][][][] e=3+5=8, n=5, a_n=8, prime=2
        # 22|2|22|22|2  find 4 | that split 8 prime number, select 4 positions from 7 positions => C(7,4) = C(n+e-1, n-1) = C(n+e-1, n+e-1-(n-1)) = C(n+e-1, e)
        # C(n+e-1, e) = (n+e-1)!/(e! * (n-1)!) # every prime number prime_i^e will have C(n+e-1, e) number of ways to distribute on n positions
        # for a value a_n, or product(prime_i^e), there are product(C(n+e-1, e)) ways to distribute on n positions <=> the number of ways to form an array_b 
        # the number of arr_b <=> for val in range(1, maxValue): sum of the number of ways to form an array_b with value a_n = val
        # maxValue <= 10^4 < 2^{14} prime number 2, prime number count e < 14
        m = n + 14
        factorial = [1] * (m+1)
        for i in range(2, m+1):
            factorial[i] = factorial[i-1] * i % MOD # large number multiplication is time-consuming
        inverse_factorial = [1] * (m + 1)
        inverse_factorial[m] = pow(factorial[m], MOD-2, MOD) 
        # 1/n! * n = 1/(n-1)!
        for i in range(m-1, -1, -1):
            inverse_factorial[i] = inverse_factorial[i+1] * (i+1) % MOD
        
        def C(n, k):
            return factorial[n] * inverse_factorial[k] % MOD * inverse_factorial[n-k] % MOD
        # get the smallest prime factor of value
        spf = list(range(1 + maxValue)) # the smallest prime number 2
        for p in range(2, int((1+maxValue)**(0.5))+1):
            if spf[p] == p:
                for i in range(p*p, 1+maxValue, p):
                    # find all of the values that  are divisible by prime number p
                    if spf[i] == i:
                        spf[i] = p
        
        res = 0
        for i in range(1, 1+maxValue):
            x, ways = i, 1 # number of ways value x can be distributed on n positions
            while x > 1:
                p = spf[x]
                count = 0
                while x % p == 0:
                    x //= p
                    count += 1
                # number of ways to distribute count of prime numbers p on n positions
                ways = ways * C(n+count-1, count) % MOD # number x can be represented by product of prime^{count}
            # every number x will have an arr_b <=> an arr_a
            res = (res + ways) % MOD
        return res 
