class Solution:
    def numberToWords(self, num: int) -> str:
        # 1 234 567
        digits = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        def get_words_rep(val):
            # takes a number less than 1000 and convert just that chunk to words.
            res = []
            if val >= 100:
                tmp = val // 100
                res.append(digits[tmp])
                res.append('Hundred')
                val -= tmp * 100
            if val >= 20:
                tmp = val // 10
                res.append(tens[tmp - 1])
                val -= tmp * 10
            if 10 <= val and val < 20:
                res.append(teens[val - 10])
            if 0 < val and val < 10:
                res.append(digits[val])
        
            return res

        if num == 0: return 'Zero'
        # 1 000 010
        groups = ['', 'Thousand', 'Million', 'Billion']
        res = []
        # 2 147 483 647 there are at most 4 groups
        unit = int(1e9)
        while num:
            for i in range(3, -1, -1):
                val = num // unit
                if val == 0:
                    unit //= 1000
                    continue
                group_rep = get_words_rep(val)
                res.extend(group_rep)
                if i != 0:
                    res.append(groups[i])
                num -= unit * val
                unit //= 1000

        return ' '.join(res)
