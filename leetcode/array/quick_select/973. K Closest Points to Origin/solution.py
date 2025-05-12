class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_dist(p):
            return p[0]*p[0] + p[1]*p[1]
        
        def findKth(l, r, k):
            if l == r:
                return l
            tmp_ind = l + (r - l) // 2
            pivot = cal_dist(points[tmp_ind])
            i, j = l, r
            while i <= j:
                while i <= j and cal_dist(points[i]) < pivot:
                    i += 1
                while i <= j and cal_dist(points[j]) > pivot:
                    j -= 1
                if i <= j:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                    j -= 1
            # l --- j -- i --- r
            if l + k - 1 <= j:
                return findKth(l, j, k)
            if l + k - 1 >= i:
                return findKth(i, r, k - (i - l))
            return j + 1
        
        ind = findKth(0, len(points) - 1, k)
        return points[:ind+1]
