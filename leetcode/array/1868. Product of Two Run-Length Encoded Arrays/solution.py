class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ind1, ind2 = 0, 0
        l1, l2 = len(encoded1), len(encoded2)
        res = []
        val1, val2 = encoded1[ind1], encoded2[ind2]
        while ind1 < l1 and ind2 < l2:
            lmin = min(val1[1], val2[1])
            tempval = val1[0] * val2[0]
            if not res:
                res.append([tempval, lmin])
            else:
                if res[-1][0] == tempval:
                    res[-1][1] += lmin
                else:
                    res.append([tempval, lmin])
            val1[1] -= lmin
            val2[1] -= lmin
            if val1[1] == 0:
                ind1 += 1
                if ind1 < l1:
                    val1 = encoded1[ind1]
            if val2[1] == 0:
                ind2 += 1
                if ind2 < l2:
                    val2 = encoded2[ind2]
        
        return res
