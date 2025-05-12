class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # rowConditions -> {value: row_ind},  colConditions -> {value: col_ind}
        # to get the index of the value, build a graph, get the topological sort of the values
        # for the values that didn't appear at the conditions, graph[val] = [], indegree[val] = 0
        def get_val_index(conds):
            val_index = {}
            graph = collections.defaultdict(list)
            indegree = collections.defaultdict(int)
            for val1, val2 in conds:
                graph[val1].append(val2)
                indegree[val2] += 1
                indegree[val1] = indegree.get(val1, 0)
            for i in range(1, k+1):
                if i not in graph:
                    graph[i] = []
                if i not in indegree:
                    indegree[i] = 0
            que = collections.deque([])
            for val, indg in indegree.items():
                if indg == 0:
                    que.append(val)
            ind = 0
            while que:
                val = que.popleft()
                val_index[val] = ind
                ind += 1
                for nex in graph[val]:
                    indegree[nex] -= 1
                    if indegree[nex] == 0:
                        que.append(nex)
            return val_index if len(val_index) == k else None

        val_index_row = get_val_index(rowConditions)
        val_index_col = get_val_index(colConditions)
        if val_index_row is None or val_index_col is None:
            return []
        res = [[0] * k for _ in range(k)]
        for val, row in val_index_row.items():
            col = val_index_col[val]
            res[row][col] = val
        return res
