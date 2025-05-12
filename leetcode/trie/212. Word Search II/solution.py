class TrieNode:
    # retrieve
    def __init__(self, val=None, isword=False):
        self.val = val
        self.isword = isword
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode(c)
            p = p.children[c]
        p.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
    
        m, n = len(board), len(board[0])
    
        res = set()
        # use trie to prune the dfs
        def dfs(trienode, curx, cury, curpath):
            if trienode.isword:
                res.add(''.join(curpath))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = curx + dx, cury + dy
                if not (-1 < nx < m and -1 < ny < n):
                    continue
                if board[nx][ny] == '0':
                    continue
                tmpval = board[nx][ny]
                if tmpval not in trienode.children:
                    continue
                board[nx][ny] = '0'
                curpath.append(tmpval)
                dfs(trienode.children[tmpval], nx, ny, curpath)
                curpath.pop()
                board[nx][ny] = tmpval
        
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c not in trie.root.children:
                    continue
                board[i][j] = '0'
                dfs(trie.root.children[c], i, j, [c])
                board[i][j] = c
        return list(res)
