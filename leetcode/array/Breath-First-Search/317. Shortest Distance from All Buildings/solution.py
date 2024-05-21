class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance_to_buildings = [[0] * n for _ in range(m)]
        count_visited_buildings = [[0] * n for _ in range(m)]
        count_of_buildings = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                count_of_buildings += 1
                que = collections.deque([(i, j, 0)])
                v = [[False] * n for _ in range(m)]
                v[i][j] = True
                while que:
                    x, y, dist = que.popleft()
                    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        nx, ny = x + dx, y + dy
                        if not (-1 < nx < m and -1 < ny < n):
                            continue
                        if v[nx][ny]:
                            continue
                        if grid[nx][ny] != 0:
                            continue
                        count_visited_buildings[nx][ny] += 1
                        distance_to_buildings[nx][ny] += dist + 1
                        que.append((nx, ny, dist + 1))
                        v[nx][ny] = True

        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                if count_visited_buildings[i][j] != count_of_buildings:
                    continue
                res = min(distance_to_buildings[i][j], res)
        return res if res != float('inf') else -1       
