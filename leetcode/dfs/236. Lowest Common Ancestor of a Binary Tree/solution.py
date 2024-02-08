# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def dfs(node):
            nonlocal res
            if not node:
                return False
            leftfind = dfs(node.left)
            rightfind = dfs(node.right)
            currfind = node.val == p.val or node.val == q.val
            if (leftfind + rightfind + currfind) == 2 and res is None:
                res = node
            return currfind or leftfind or rightfind
        
        dfs(root)
        
        return res

