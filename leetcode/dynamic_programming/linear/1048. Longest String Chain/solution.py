class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_len = len(words)
        res = 0
        word_chain_len = {}
        words.sort(key=len)
        word_chain_len[''] = 0

        for word in words:
            word_chain_len[word] = 1
            n = len(word)
            for i in range(n):
                word_new = word[:i] + word[i+1:]
                if word_new in word_chain_len:
                    word_chain_len[word] = max(word_chain_len[word], word_chain_len[word_new] + 1)
                res = max(res, word_chain_len[word])

        return res 