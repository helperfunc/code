class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows, cols = len(image), len(image[0])

        def binary_search_col(row_a, row_b, col_a, col_b, find_with_black_pixels=True):
            if col_a > col_b: # y+1 > n-1
                return cols
            l, r = col_a, col_b
            while l + 1 < r:
                m = l + (r - l) // 2
                has_black_pixel = False
                for i in range(row_a, row_b+1):
                    if image[i][m] == '1':
                        has_black_pixel = True
                        break
                if has_black_pixel == find_with_black_pixels:
                    r = m
                else:
                    l = m
            has_black_pixel = False
            for i in range(row_a, row_b+1):
                if image[i][l] == '1':
                    has_black_pixel = True
                    break
            if has_black_pixel == find_with_black_pixels:
                return l
            has_black_pixel = False
            for i in range(row_a, row_b+1):
                if image[i][r] == '1':
                    has_black_pixel = True
                    break
            if has_black_pixel == find_with_black_pixels:
                return r
            return cols

        def binary_search_row(row_a, row_b, col_a, col_b, find_with_black_pixels=True):
            if row_a > row_b: # x+1 > n-1
                return rows
            l, r = row_a, row_b
            while l + 1 < r:
                m = l + (r - l) // 2
                has_black_pixel = False
                for j in range(col_a, col_b+1):
                    if image[m][j] == '1':
                        has_black_pixel = True
                        break
                if has_black_pixel == find_with_black_pixels:
                    r = m
                else:
                    l = m
            has_black_pixel = False
            for j in range(col_a, col_b+1):
                if image[l][j] == '1':
                    has_black_pixel = True
                    break
            if has_black_pixel == find_with_black_pixels:
                return l
            has_black_pixel = False
            for j in range(col_a, col_b+1):
                if image[r][j] == '1':
                    has_black_pixel = True
                    break
            if has_black_pixel == find_with_black_pixels:
                return r
            return rows

        left = binary_search_col(0, rows-1, 0, y, find_with_black_pixels=True)
        right = binary_search_col(0, rows-1, y+1, cols-1, find_with_black_pixels=False)
        top = binary_search_row(0, x, left, right-1, find_with_black_pixels=True)
        bottom = binary_search_row(x+1, rows-1, left, right-1, find_with_black_pixels=False)
        return (right - left) * (bottom - top)
