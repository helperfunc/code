class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int) # length of this is the length of letters
        n = len(words)
        for c in words[0]:
            indegree[c] = 0
        # build the graph from the letters
        for i in range(n-1):
            w1, w2 = words[i], words[i+1]
            for c in w2:
                if c not in indegree:
                    indegree[c] = 0
            wlen = min(len(w1), len(w2))
            for j in range(wlen):
                invalid = True
                if w2[j] in graph[w1[j]]:
                    invalid = False
                    break
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                    invalid = False
                    break
            if invalid and len(w1) > len(w2):
                return ''
        # topological sort
        res = [] # the topological sort of the letters
        que = collections.deque([])
        for letter, v in indegree.items():
            if v == 0:
                que.append(letter)
        while que:
            letter = que.popleft()
            res.append(letter)
            for nex in graph[letter]:
                indegree[nex] -= 1
                if indegree[nex] == 0:
                    que.append(nex)
        return ''.join(res) if len(res) == len(indegree) else ''
