class BinaryIndexTree:
    def __init__(self, n):
        # n the length of the array
        self.tree = [0] * (n+1) # 1-index tree, [1  10  11  100], count
    
    def update(self, index, count):
        # update the number of values before the index value for index to the root node
        index += 1 # update 0-index to 1-index
        while index < len(self.tree):
            self.tree[index] += count
            index += index & (-index) # the last index of 1, for example 100 & (~100+1) = 100
    
    def query(self, index):
        # to find the count from the current index subtree
        index += 1
        current_sum = 0
        while index > 0:
            current_sum += self.tree[index]
            index -= index & (-index)
        return current_sum

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        if n < 3: return 0
        
        pos2 = [0] * n # {nums2 value: nums2 index}
        for i in range(n):
            pos2[nums2[i]] = i

        bit1 = BinaryIndexTree(n)
        left_counts = [0] * n
        for x in nums1:
            # the number of values x appears before the value nums2[pos] in both of nums1 and nums2
            pos = pos2[x]
            left_counts[x] = bit1.query(pos)
            bit1.update(pos, 1)
        
        bit2 = BinaryIndexTree(n)
        right_counts = [0] * n
        for x in reversed(nums1):
            pos = pos2[x]
            right_counts[x] = bit2.query(n - 1) - bit2.query(pos)  # left of n-1 - left of pos -> right of pos, from pos to n-1
            bit2.update(pos, 1)
        
        return sum(left_counts[x] * right_counts[x] for x in range(n))
