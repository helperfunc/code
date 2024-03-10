import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # h = []
        # n = len(nums)
        # res = []
        # for i in range(n):
        #     # ensure that the maximum value from the heap would be within the sliding window
        #     # not all of the values in the heap are from current sliding window
        #     heapq.heappush(h, (-nums[i], i))
        #     while h and h[0][1] < i - k + 1: #<minimum valid index of the sliding window
        #         heapq.heappop(h)
        #     if not res:
        #         if i == k - 1:
        #             res.append(-h[0][0])
        #     else:
        #         res.append(-h[0][0])
        # return res
        
        # monotonic queue
        # only saves the value that is larger than the current value,
        # the maximum value from the queue is the value at 0 position
        # while the maximum value is not from current sliding window, pop this value
        q = collections.deque([])
        n = len(nums)
        res = []
        for i in range(n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            while q and q[0] < i - k + 1:
                q.popleft()
            if not res:
                if i == k - 1:
                    res.append(nums[q[0]])
            else:
                res.append(nums[q[0]])
        return res
