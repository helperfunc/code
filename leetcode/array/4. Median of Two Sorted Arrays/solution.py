class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [1,3]
        #    i
        # [2]
        #  j

        # [1,2]
        #      i
        # [3,4]
        #  j
        m, n = len(nums1), len(nums2)

        def findKth(i, j, k):
            if i == m:
                return nums2[j + k - 1]
            if j == n:
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])
            
            val1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < m else None
            val2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < n else None
            if val2 is None or (val1 and val1 < val2):
                return findKth(i + k // 2, j, k - k//2)
            return findKth(i, j + k // 2, k - k//2)

        if (m + n) % 2 == 1:
            return findKth(0, 0, (m + n) // 2 + 1)
        else:
            return (findKth(0, 0, (m + n) // 2) + findKth(0, 0, (m + n) // 2 + 1)) / 2
        
