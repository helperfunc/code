import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 1.binary search to insert new value and delete old value that is not within the current sliding window
        # time complexity O(nk)
        # 2.heaps, smaller values to a max heap and large values to a min heap.
        # the median is calculated from the front of these two heaps
        # O(nlogn)
        n = len(nums)
        window = sorted(nums[:k])
        def get_median():
            if k % 2 == 1:
                return window[k // 2]
            else:
                return (window[k // 2] + window[k // 2 - 1]) * 0.5
        res = [get_median()]
        for i in range(k, n):
            bisect.insort(window, nums[i]) # bisect_left() to find the index to insert nums[i]
            del window[bisect.bisect_left(window, nums[i - k])] # bisect_left() to find the index, window[:index] < value <= window[index:]
            res.append(get_median())
        return res
