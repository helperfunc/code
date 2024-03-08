class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        def binary_search(row, val):
            l, r = 0, n - 1
            while l + 1 < r:
                m = l + (r - l)//2
                if row[m] == val:
                    return m
                if row[m] < val:
                    l = m
                else:
                    r = m
            if row[l] == val:
                return l
            if row[r] == val:
                return r
            return -1
        
        for val in mat[0]:
            r = 1
            count = 1
            while r < m:
                ind = binary_search(mat[r], val)
                if ind != -1:
                    count += 1
                    r += 1
                else:
                    break
            if count == m:
                return val
        
        return -1
