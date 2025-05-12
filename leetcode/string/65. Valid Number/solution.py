class Solution:
    def isNumber(self, s: str) -> bool:
        isdigit, issign, ise, isdot = False, False, False, False
        # while the character is sign, 
        # (isdigit == false && issign == false) or (ise and previous character is 'e' or 'E' and current pos is not the last character)
        # while the character is e
        # isdigit == true and current pos is not the last
        # while the character is dot
        # (isdot == false)
        for i, c in enumerate(s):
            if c.isdigit():
                isdigit = True
                continue
            if c == '+' or c == '-':
                #if i != len(s) - 1 and (isdigit == False and issign == False and ise == False and isdot == False) or (ise and i > 0 and s[i - 1].lower() == 'e' and i != len(s) - 1):
                if (i == 0 or (ise and i > 0 and s[i - 1].lower() == 'e')) and i != len(s) - 1:
                    issign = True
                    continue
                else:
                    return False
            if c.lower() == 'e':
                if (isdigit and i != len(s) - 1 and ise == False):
                    ise = True
                    continue
                else:
                    return False
            if c == '.':
                if (isdot == False and ise == False and (i != len(s) - 1 or isdigit)):
                    isdot = True
                    continue
                else:
                    return False
            return False
        
        return True

