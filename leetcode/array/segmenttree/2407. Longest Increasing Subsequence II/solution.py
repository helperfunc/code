class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        # # dp[i] - the length of the longest subsequence that ended at i
        # # dp[i] = max(dp[i], dp[j] + 1) j < i and 0 < nums[i] - nums[j] <= k
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if 0 < nums[i] - nums[j] <= k:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)
        class Node:
            def __init__(self, l, r):
                self.l, self.r = l, r
                self.tmplen = 0
                if l + 1 == r:
                    return
                m = l + (r - l) // 2
                self.left = Node(l, m)
                self.right = Node(m, r)
            
            def find(self, l, r):
                # to find the length of the longest subsequence of the interval
                if self.l == l and self.r == r:
                    return self.tmplen
                m = self.l + (self.r - self.l) // 2
                if l >= m:
                    return self.right.find(l, r) # go to right tree to find interval
                elif r <= m:
                    return self.left.find(l, r)
                else:
                    # l < m < r
                    return max(self.left.find(l, m), self.right.find(m, r))
            
            def insert(self, val, tmplen):
                # val is the value from the interval
                if self.l + 1 == self.r:
                    # the current node only contains a value
                    self.tmplen = tmplen
                    return
                m = self.l + (self.r - self.l) // 2
                if val >= m:
                    # [self.l   m  val  self.r]
                    self.right.insert(val, tmplen)
                else:
                    self.left.insert(val, tmplen)
                # update the tmplen
                self.tmplen = max(self.left.tmplen, self.right.tmplen)
                
        # find the length of the longest subsequence with O(logn)
        val_min, val_max = min(nums), max(nums)
        # [val_min, val_max] -> val to be the length of the longest subsequence
        # [val_min, (val_min + val_max) // 2]  [(val_min + val_max) // 2, val_max]
        # find the length of the longest subsequence 
        # the value from [nums[i] - k, nums[i]]
        node = Node(val_min, val_max + 1)
        res = 0
        for num in nums:
            if num == val_min:
                tmplen = 0
            else:
                tmplen = node.find(max(num - k, val_min), num)
                # find the length of the longest subsequence from the value interval
            res = max(res, tmplen + 1)
            node.insert(num, tmplen + 1)
        return res
