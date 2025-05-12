import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        n = len(nums)
        res = []
        for i in range(n):
            # ensure that the maximum value from the heap would be within the sliding window
            # not all of the values in the heap are from current sliding window
            heapq.heappush(h, (-nums[i], i))
            while h and h[0][1] < i - k + 1: #<minimum valid index of the sliding window
                heapq.heappop(h)
            if not res:
                if i == k - 1:
                    res.append(-h[0][0])
            else:
                res.append(-h[0][0])
        return res
            
