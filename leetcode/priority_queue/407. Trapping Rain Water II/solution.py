class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # save the height of the boarder to a heapq
        # pop the minimum value from the heapq
        # compare the new cell height with the minimum value, get the volume of water
        m, n = len(heightMap), len(heightMap[0])
        height_pos_cell = []
        v = [[False] * n for _ in range(m)]

        for i in range(n):
            heapq.heappush(height_pos_cell, [heightMap[0][i], 0, i])
            v[0][i] = True
            heapq.heappush(height_pos_cell, [heightMap[m-1][i], m-1, i])
            v[m - 1][i] = True
        for i in range(m):
            heapq.heappush(height_pos_cell, [heightMap[i][0], i, 0])
            v[i][0] = True
            heapq.heappush(height_pos_cell, [heightMap[i][n-1], i, n - 1])
            v[i][n - 1] = True
        res = 0
        while height_pos_cell:
            tmph, tmpx, tmpy = heapq.heappop(height_pos_cell)
            v[tmpx][tmpy] = True
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = tmpx + dx, tmpy + dy
                if -1 < nx < m and -1 < ny < n and v[nx][ny] == False:
                    # print((nx, ny, tmph, tmpx, tmpy, heightMap[nx][ny]))
                    res += max(0, tmph - heightMap[nx][ny]) # tmph is the minimum height
                    heapq.heappush(height_pos_cell, [max(heightMap[nx][ny], tmph), nx, ny])
                    v[nx][ny] = True
        return res
