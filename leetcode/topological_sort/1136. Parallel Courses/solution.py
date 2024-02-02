class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        que = collections.deque([])
        graph = collections.defaultdict(list)
        indeg = {i: 0 for i in range(1, n+1)}
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            indeg[nextCourse] += 1
        
        count = 0
        for k, v in indeg.items():
            if indeg[k] == 0:
                que.append(k)
                count += 1
        
        res = 0
        while que:
            for _ in range(len(que)):
                course = que.popleft()
                for nex in graph[course]:
                    indeg[nex] -= 1
                    if indeg[nex] == 0:
                        que.append(nex)
                        count += 1
            res += 1
        return res if count == n else -1

