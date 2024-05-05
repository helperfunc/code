class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_ind = {0:-1}
        reminder = 0
        for i, num in enumerate(nums):
            reminder = (reminder + num) % k
            if reminder in reminder_ind:
                preind = reminder_ind[reminder]
                if i - preind >= 2:
                    return True
            else:
                reminder_ind[reminder] = i

        return False
