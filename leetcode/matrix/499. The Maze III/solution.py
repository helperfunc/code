class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # [
        #  [0,0,0,0,b,0,0],
        #  [0,0,1,0,0,1,0],
        #  [h,0,0,0,1,0,0],
        #  [0,0,0,0,0,0,1]
        # ]
        m, n = len(maze), len(maze[0])
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        directions_instr = ['d', 'r', 'l', 'u']
        distances = [[float('inf')] * n for _ in range(m)]
        distances[ball[0]][ball[1]] = 0 
        instructions = [['z'] * n for _ in range(m)]
        instructions[ball[0]][ball[1]] = ''
        h = []
        heapq.heappush(h, [[ball, ''], 0])
        while h:
            (pos, instruc), dist = heapq.heappop(h)
            i, j = pos
            if distances[i][j] < dist or (distances[i][j] == dist and instructions[i][j] < instruc):
                continue # already get the shortest distance or lexicographically minimum instruction
            for ind, (dx, dy) in enumerate(directions):
                count = 0 # number of empty spaces traveled
                nx, ny = i + dx, j + dy
                while (-1 < nx < m and -1 < ny < n) and maze[nx][ny] == 0:
                    if (-1 < nx < m and -1 < ny < n) and nx == hole[0] and ny == hole[1]:
                        nx += dx
                        ny += dy
                        count += 1
                        break
                    nx += dx
                    ny += dy
                    count += 1
                nx -= dx
                ny -= dy
                if distances[nx][ny] > distances[i][j] + count or (distances[nx][ny] == distances[i][j] + count and instructions[nx][ny] > instructions[i][j] + directions_instr[ind]):
                    distances[nx][ny] = distances[i][j] + count
                    instructions[nx][ny] = instructions[i][j] + directions_instr[ind]
                    heapq.heappush(h, [[[nx, ny], instructions[i][j]], distances[nx][ny]])
        return instructions[hole[0]][hole[1]] if distances[hole[0]][hole[1]] != float('inf') else 'impossible'
      
