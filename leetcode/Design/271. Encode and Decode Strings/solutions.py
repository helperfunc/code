class Codec:
    def encode_len_str(self, s):
        l = len(s) # 32-bit integer, 4 bytes, 8-bit per byte
        res = []
        for i in range(4):
            tmp = (l >> (i * 8) & 0xff)  # right move integer l 0, 8, 16, 24, use 0xff to only save the last 8-bits value of 1
            res.append(chr(tmp)) #and use unicode to represent the 8-bits
        res.reverse()
        return ''.join(res)

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # add the length of the string before string s
        # add a fixed length that represent the length of the string
        # use 4 bytes to represent the length number 
        res = []
        for s in strs:
            res.append(self.encode_len_str(s))
            res.append(s)
        return ''.join(res)
        
    def decode_len_str(self, s):
        res = 0
        for c in s:
            res = res * 256 + ord(c) # pow(2,8) = 256, the decoded unicode character
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        while i < len(s):
            tmp_s_len = s[i:i+4]
            tmp_len_int = self.decode_len_str(tmp_s_len)
            i += 4
            tmp_s = s[i:i+tmp_len_int]
            res.append(tmp_s)
            i += tmp_len_int
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
