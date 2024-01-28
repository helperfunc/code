class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res = 0
        n = len(bombs)
        def dist_sq(pos1, pos2):
            diff1 = pos1[0] - pos2[0]
            diff2 = pos1[1] - pos2[1]
            return diff1 * diff1 + diff2 * diff2
        
        def dfs(ind, v):
            cx, cy, cr = bombs[ind]
            for i in range(n):
                if i in v:
                    continue
                if i == ind:
                    continue
                nx, ny, nr = bombs[i]
                tmp_dist = dist_sq((cx, cy), (nx, ny))
                if tmp_dist <= cr * cr:
                    v.add(i)
                    dfs(i, v)
                    # v.remove(i)

        for i in range(n):
            v = set([i])
            dfs(i, v)
            res = max(res, len(v))
        
        return res


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        res = 0

        def dist_sq(pos1, pos2):
            diff1, diff2 = pos1[0] - pos2[0], pos1[1] - pos2[1]
            return diff1 * diff1 + diff2 * diff2

        def dfs(ind, v):
            cx, cy, cr = bombs[ind]

            # for i in range(n):
            for i in graph[ind]:
                # if ind == i:
                #     continue
                if i in v:
                    continue
                nx, ny, nr = bombs[i]
                # tmp_dist = dist_sq((cx, cy), (nx, ny))
                # if tmp_dist <= cr * cr:
                v.add(i)
                dfs(i, v)
        
        # for i in range(n):
        #     v = set([i])
        #     dfs(i, v)
        #     res = max(res, len(v))
        graph = collections.defaultdict(list)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                x2, y2, r2 = bombs[j]
                if dist_sq((x1, y1), (x2, y2)) <= r1 * r1:
                    graph[i].append(j)

        for i in range(n):
            v = set([i])
            dfs(i, v)
            res = max(res, len(v))
        
        return res
