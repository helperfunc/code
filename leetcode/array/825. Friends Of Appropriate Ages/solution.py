# O(nlogn)
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # age[y] <= 0.5 * age[x] + 7                age[y] > 0.5 * age[x] + 7
        # age[y] > age[x]                           age[y] <= age[x] # the last age[y] <= age[x]
        # age[y] > 100 && age[x] < 100
        ages.sort()
        res = 0
        n = len(ages)

        def binary_search_larger_than(val, left, right):
            if not (-1 < left < n and -1 < right < n):
                return -1
            l, r = left, right
            while l + 1 < r:
                m = l + (r - l) // 2
                if ages[m] < val:
                    l = m
                elif ages[m] == val:
                    l = m
                else:
                    r = m
            if ages[l] > val:
                return l
            if ages[r] > val:
                return r
            return -1

        def binary_search_less_equal(val, left, right):
            if not (-1 < left < n and -1 < right < n):
                return -1
            l, r = left, right
            while l + 1 < r:
                m = l + (r - l) // 2
                if ages[m] < val:
                    l = m
                elif ages[m] == val:
                    l = m
                else:
                    r = m
            if ages[r] <= val:
                return r
            if ages[l] <= val:
                return l
            return -1

        for i, age in enumerate(ages):
            val = int(0.5 * age) + 7
            lower = binary_search_larger_than(val, 0, i)
            upper = binary_search_less_equal(age, i, n - 1)
            if lower != -1 and upper != -1:
                res += upper - lower # not include themself

        return res

# use age range
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        ages_count = [0] * 121
        for age in ages:
            ages_count[age] += 1

        for i in ages:
            if ages_count[i] == 0: continue
            val = int(0.5 * i) + 7
            for age in range(val + 1, i + 1):
                if ages_count[age] > 0:
                    res += ages_count[age]
                if age == i:
                    res -= 1
        return res

# use prefix sum O(n)
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        ages_count = [0] * 121
        for age in ages:
            ages_count[age] += 1

        pref_sum = [0] * 121
        for i in range(1, 121):
            pref_sum[i] = pref_sum[i - 1] + ages_count[i]

        for i in ages:
            if ages_count[i] == 0: continue
            val = int(0.5 * i) + 7
            # for age in range(val + 1, i + 1):
            #     if ages_count[age] > 0:
            #         res += ages_count[age]
            #     if age == i:
            #         res -= 1
            if i > val:
                res += pref_sum[i] - pref_sum[val] - 1
        return res

# O(1)
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        ages_count = [0] * 121
        for age in ages:
            ages_count[age] += 1

        pref_sum = [0] * 121
        for i in range(1, 121):
            pref_sum[i] = pref_sum[i - 1] + ages_count[i]

        # for i in ages:
        for i in range(1, 121):
            if ages_count[i] == 0: continue
            val = int(0.5 * i) + 7
            # for age in range(val + 1, i + 1):
            #     if ages_count[age] > 0:
            #         res += ages_count[age]
            #     if age == i:
            #         res -= 1
            if i > val:
                res += (pref_sum[i] - pref_sum[val] - 1) * ages_count[i]
        return res
