class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # [[0,2],[5,10],[13,23],[24,25]]
        #                                i
        # [[1,5],[8,12],[15,24],[25,26]]
        #                         j
        l1, l2 = len(firstList), len(secondList)
        i, j = 0, 0
        res = []
        while i < l1 and j < l2:
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if left <= right:
                res.append([left, right])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
