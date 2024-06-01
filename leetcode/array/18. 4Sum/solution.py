class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # to get unique quadruplets
        n = len(nums)
        res = []
        # iterate a, b and use two pointers to find value c and d
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target: break
            if nums[a] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target: continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                if nums[a] + nums[b] + nums[b + 1] + nums[b + 2] > target: break
                if nums[a] + nums[b] + nums[n - 1] + nums[n - 2] < target: continue
                l, r = b + 1, n - 1
                while l < r:
                    temp = nums[a] + nums[b] + nums[l] + nums[r]
                    if temp < target:
                        l += 1
                    elif temp > target:
                        r -= 1
                    else:
                        res.append([nums[a],nums[b],nums[l],nums[r]])
                        while l < r:
                            if nums[l] == nums[l + 1]:
                                l += 1
                            else:
                                l += 1
                                break
                        while l < r:
                            if nums[r] == nums[r - 1]:
                                r -= 1
                            else:
                                r -= 1
                                break
        return res
