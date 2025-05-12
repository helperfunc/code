class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # lower-nums[i]<= nums[j]<=upper-nums[i]
        # find index i1 nums[i] >= lower - nums[j] # find the lowest possible i1
        # find index i2 nums[i] > upper - nums[j] # find the lowest possible i2
        # res += i2 - i1
        def binary_search(arr, target, start, end, equal=True):
            # find the lowest possible index where nums[index] >= target (equal = True)
            l, r = start, end - 1 # r > -1
            while l + 1 < r:
                m = l + (r - l) // 2
                if arr[m] == target:
                    if equal:
                        r = m
                    else:
                        l = m
                elif arr[m] < target:
                    l = m
                else:
                    r = m
            if equal:
                if arr[l] >= target:
                    return l
                if r > -1 and arr[r] >= target:
                    return r
                return end # the length of the arr
            else:
                if arr[l] > target:
                    return l
                if r > -1 and arr[r] > target:
                    return r
                return end

        nums.sort()
        res = 0
        for j in range(len(nums)):
            i1 = binary_search(nums, lower - nums[j], 0, j)
            i2 = binary_search(nums, upper - nums[j], 0, j, equal=False) 
            # i2 previous index is the last index of the good pairs
            res += i2 - i1 # number of good pairs
        return res
