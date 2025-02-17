class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        isstable = False
        while isstable == False:
            # crush the candies simultaneously and update vertical values of the board use the none-zero values
            # array to save the candies positions that should be crushed.
            candies_crushed = []
            m, n = len(board), len(board[0])
            # for every row, find the same type of candies that have the length >= 3
            for i in range(m):
                j, k = 0, 0
                while j < n:
                    prev_val = board[i][j]
                    k += 1
                    if k < n and prev_val != 0 and board[i][k] == prev_val:
                        continue
                    if k - j >= 3:
                        for l in range(j, k):
                            candies_crushed.append([i, l])
                    j = k
            # for every column, find the same type of candies that have the length >= 3
            for i in range(n):
                j, k = 0, 0
                while j < m:
                    prev_val = board[j][i]
                    k += 1
                    if k < m and prev_val != 0 and board[k][i] == prev_val:
                        continue
                    if k - j >= 3:
                        for l in range(j, k):
                            candies_crushed.append([l, i])
                    j = k
            
            # update board using the crushed candies
            if len(candies_crushed) == 0:
                isstable = True
                break

            # get the updated columns using the non-zero values
            for i, j in candies_crushed:
                board[i][j] = 0
                
            # update the board
            cols_vals = []
            for i in range(n):
                tmp = []
                for j in range(m):
                    if board[j][i] != 0:
                        tmp.append(board[j][i])
                cols_vals.append(tmp)

            for i in range(n):
                arr = [0] * (m - len(cols_vals[i])) + cols_vals[i]
                for j in range(m):
                    board[j][i] = arr[j]
  
        return board
