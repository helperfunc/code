class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # [0,1,0]
        #  use a deque to save the left index of the previous flippeed subarray
        #  while the prevous flipps is not affect the current position, popleft the index
        #  the number of flipps is len(que)
        #  if curr == 0: len(que) % 2 == 0 this current postion should be flippeed
        #  if curr == 1: len(que) % 2 == 1 this current postion should be flippeed
        #  while at current postion and this should be flipped, and the i + k > len(nums) return -1
        n = len(nums)
        q = collections.deque()
        res = 0
        for i in range(n):
            while q and q[0] + k <= i:
                q.popleft()
            if len(q) % 2 == nums[i]:
                if i + k > n:
                    return -1
                q.append(i)
                res += 1
        return res

