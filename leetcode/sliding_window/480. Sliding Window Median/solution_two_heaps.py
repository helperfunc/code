import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 1.binary search to insert new value and delete old value that is not within the current sliding window
        # time complexity O(nk)
        # 2.heaps, smaller values to a max heap and large values to a min heap.
        # the median is calculated from the front of these two heaps
        # O(nlogn)
        smaller_max_heap, large_min_heap, res = [], [], []
        n = len(nums)
        for i in range(k):
            heapq.heappush(smaller_max_heap, (-nums[i], i))
        for i in range(k//2):
            # the number of values in the smaller_max_heap > large_min_heap
            heapq.heappush(large_min_heap, (-smaller_max_heap[0][0], smaller_max_heap[0][1]))
            heapq.heappop(smaller_max_heap)
        
        def get_median():
            if k % 2 == 1:
                return -smaller_max_heap[0][0]
            else:
                return (-smaller_max_heap[0][0] + large_min_heap[0][0]) * 0.5

        res.append(get_median())
        for i in range(k, n):
            if nums[i] <= -smaller_max_heap[0][0]:
                # <= the number of values in the smaller_max_heap > large_min_heap
                # add the value to the smaller_max_heap
                # the length of the smaller_max_heap + 1
                heapq.heappush(smaller_max_heap, (-nums[i], i))
                if nums[i - k] >= -smaller_max_heap[0][0]: 
                    # re-balance the smaller_max_heap and large_min_heap
                    # the deleted value is from large_min_heap 
                    # add the value to the large_min_heap length of large_min_heap + 1
                    heapq.heappush(large_min_heap, (-smaller_max_heap[0][0], smaller_max_heap[0][1]))
                    heapq.heappop(smaller_max_heap)
            else:
                heapq.heappush(large_min_heap, (nums[i], i))
                # length of large_min_heap + 1
                if nums[i - k] <= large_min_heap[0][0]:
                    # the deleted value is from smaller_max_heap 
                    # add the value to the smaller_max_heap length of smaller_max_heap + 1
                    heapq.heappush(smaller_max_heap, (-large_min_heap[0][0], large_min_heap[0][1]))
                    heapq.heappop(large_min_heap)
            # to delete the value from the heap
            while smaller_max_heap and smaller_max_heap[0][1] < i - k + 1:
                heapq.heappop(smaller_max_heap)
            while large_min_heap and large_min_heap[0][1] < i - k + 1:
                heapq.heappop(large_min_heap)
            
            res.append(get_median())
        return res

