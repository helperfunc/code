class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if not (-1 < i < m and -1 < j < n):
                return
            if board[i][j] != 'M' and board[i][j] != 'E':
                return
            count_mines = 0
            for dx, dy in [(1, 0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]:
                nx, ny = i + dx, j + dy
                if not (-1 < nx < m and -1 < ny < n):
                    continue
                if board[nx][ny] == 'M':
                    count_mines += 1
            if count_mines > 0:
                board[i][j] = str(count_mines)
                return
            board[i][j] = 'B'
            for dx, dy in [(1, 0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]:
                nx, ny = i + dx, j + dy
                if not (-1 < nx < m and -1 < ny < n):
                    continue
                if board[nx][ny] == 'E':
                    dfs(nx, ny)
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0], click[1])
        return board
