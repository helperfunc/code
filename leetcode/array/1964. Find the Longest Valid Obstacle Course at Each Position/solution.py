class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # return ans is for every 0 to i array, find the length of the longest ascending array (larger than or equal to)
        # out_arr = [] # ascending ordered
        # if not out_arr or arr[i] > out_arr[-1]: 
        #     out_arr.append(arr[i])
        #     [1,5]
        #     [1,5,6]
        # else:
        #     # find the index from out_arr that is less than or equal to the current value arr[i]
        #     -1, out_arr[-1+1] = arr[i] -> [1]
        #     0, out_arr[0+1] = arr[i] -> [1,4]
        #     0, out_arr[0+1] = arr[i] -> [1, 2]
        out_arr = []
        res = []
        
        def binary_search_less_eq(arr, target):
            l, r = 0, len(arr) - 1
            while l + 1 < r:
                m = l + (r-l)//2
                if arr[m] == target:
                    l = m
                elif arr[m] < target:
                    l = m
                else:
                    r = m
            if arr[r] <= target:
                return r
            if arr[l] <= target:
                return l
            return -1

        for i in range(len(obstacles)):
            if not out_arr or obstacles[i] >= out_arr[-1]:
                out_arr.append(obstacles[i])
                res.append(len(out_arr))
            else:
                ind = binary_search_less_eq(out_arr, obstacles[i])
                # ind for this is surely less than len(out_arr) - 1
                out_arr[ind + 1] = obstacles[i]
                res.append(ind + 2)
        return res
