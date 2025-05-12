class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            pref_sum[i + 1] = pref_sum[i] + num
        pref_sum_set = collections.defaultdict(int)
        res = 0
        for i in range(len(pref_sum)):
            val = pref_sum[i]
            if val - k in pref_sum_set:
                res += pref_sum_set[val - k]
            pref_sum_set[val] += 1
        return res
        # pref_sum[i] - pref_sum[j] = k

