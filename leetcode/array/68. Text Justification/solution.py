class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # calculate the number of words in each line
        # distribute spaces among these words
        cur_words = [] # current words in current line
        cur_len = 0 # the total length of words in current line
        res = []
        for word in words:
            if cur_len + len(word) + len(cur_words) <= maxWidth:
                cur_words.append(word)
                cur_len += len(word)
            else:
                res.append(self.distribute_spaces(cur_words, cur_len, maxWidth))
                cur_words = [word]
                cur_len = len(word)
        if cur_words:
            # these words in the last line
            res.append(' '.join(cur_words) + ' ' * (maxWidth - cur_len - (len(cur_words) - 1)))
        return res

    def distribute_spaces(self, cur_words, cur_len, maxWidth):
        if len(cur_words) == 1:
            return cur_words[0] + ' ' * (maxWidth - cur_len)
        num_spaces = (maxWidth - cur_len) // (len(cur_words) - 1) # word word
        extra_space_count = (maxWidth - cur_len) % (len(cur_words) - 1) # from 0 to extra_space_count there are 1 extra space
        res = [cur_words[0]]
        for i in range(1, len(cur_words)):
            word = cur_words[i]
            if i <= extra_space_count:
                res.append(' ' * (num_spaces + 1))
            else:
                res.append(' ' * num_spaces)
            res.append(word)
        return ''.join(res)
                

