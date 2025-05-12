class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        cal_len = 0
        tmp_val = 0
        for c in abbr:
            if not c.isdigit():
                if tmp_val > 0:
                    cal_len += tmp_val
                    tmp_val = 0
                cal_len += 1
                if cal_len > len(word):
                    return False
                if word[cal_len - 1] != c:
                    return False
            else:
                if c == '0' and tmp_val == 0:
                    return False
                tmp_val = tmp_val * 10 + int(c)
        
        if tmp_val > 0:
            cal_len += tmp_val
        
        return cal_len == len(word)