class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set(map(tuple, points))
        res = float('inf')
        
        for i, p1 in enumerate(points):
            # for p2 in points:
            # the diagnal cannot be selected twice.
            for j in range(i):
                p2 = points[j]
                if p1[0] == p2[0] or p1[1] == p2[1]:
                    continue
                
                if (p1[0], p2[1]) in points_set and (p2[0], p1[1]) in points_set:
                    res = min(res, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))

        return res if res != float('inf') else 0
