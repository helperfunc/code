class Solution:
    def confusingNumber(self, n: int) -> bool:
        nstr = str(n)
        rotated_vals = []
        for c in nstr:
            cint = int(c)
            if cint in [2, 3, 4, 5, 7]:
                return False
            if c == '0' or c == '1' or c == '8':
                rotated_vals.append(c)
            elif c == '6':
                rotated_vals.append('9')
            else:
                rotated_vals.append('6')
        rotated_vals = rotated_vals[::-1]
        return int(''.join(rotated_vals)) != n
                
