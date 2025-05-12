# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            leftsum, leftcount = dfs(node.left)
            rightsum, rightcount = dfs(node.right)
            tmpsum = leftsum + rightsum + node.val 
            tmpcount = leftcount + rightcount + 1
            if tmpsum // tmpcount == node.val:
                res += 1
            return tmpsum, tmpcount
        
        dfs(root)
        return res
