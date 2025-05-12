class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # order_ind = [0] * 26
        # for i, c in enumerate(order):
        #     order_ind[ord(c) - ord('a')] = i
        
        # return ''.join(sorted(list(s), key=lambda x: order_ind[ord(x) - ord('a')]))

        s_char_count = collections.defaultdict(int)
        for c in s:
            s_char_count[c] += 1

        res = []
        order_char_set = set()
        for c in order:
            order_char_set.add(c)
            if c in s_char_count:
                res.extend([c] * s_char_count[c])

        for c in s:
            if c not in order_char_set:
                res.append(c)
        return ''.join(res)
