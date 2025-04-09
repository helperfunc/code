class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.sentence = None # save the sentence
        self.times = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sentence, times):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.sentence = sentence
        p.times += times

    def find(self, prefix):
        # find all the sentences that matched the prefix
        p = self.root
        for c in prefix:
            if c not in p.children:
                return []
            p = p.children[c]
        
        # find all the sentences with the TrieNode p as the root
        def dfs(node):
            res = []
            if node.sentence:
                res.append([node.times, node.sentence])
            # if the current node is a sentence last letter, it still can be the prefix of other sentences
            for nex in node.children.values():
                res.extend(dfs(nex))
            return res
        
        return dfs(p)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
        self.prefix = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(self.prefix, 1)
            self.prefix = ''
            return []
        else:
            self.prefix += c
            matches = self.trie.find(self.prefix)
            matches.sort(key=lambda x: (-x[0], x[1]))
            return [sentence for _, sentence in matches[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
