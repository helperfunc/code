# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        smaller_stack = [] # save the values <= target, with ascending order
        larger_stack = [] # save the values > target, with descending order
        def build_smaller_stack():
            node = root
            while node:
                if node.val <= target:
                    smaller_stack.append(node)
                    node = node.right
                else:
                    node = node.left
        def build_larger_stack():
            node = root
            while node:
                if node.val > target:
                    larger_stack.append(node)
                    node = node.left
                else:
                    node = node.right
        def get_val_smaller_stack():
            node = smaller_stack.pop()
            node = node.left # left subtree values will < node.val
            while node:
                smaller_stack.append(node)
                node = node.right
        def get_val_larger_stack():
            node = larger_stack.pop()
            node = node.right # right subtree values will > node.val
            while node:
                larger_stack.append(node)
                node = node.left

        build_smaller_stack()
        build_larger_stack()
        res = []
        for _ in range(k):
            smaller_val = smaller_stack[-1].val if smaller_stack else None
            larger_val = larger_stack[-1].val if larger_stack else None
            if smaller_val is not None and larger_val is not None:
                if abs(smaller_val - target) <= abs(larger_val - target):
                    res.append(smaller_val)
                    get_val_smaller_stack()
                else:
                    res.append(larger_val)
                    get_val_larger_stack()
            elif larger_val is not None:
                res.append(larger_val)
                get_val_larger_stack()
            elif smaller_val is not None:
                res.append(smaller_val)
                get_val_smaller_stack()
        return res
