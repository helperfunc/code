# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, cur_num):
            if not node:
                return

            if not node.left and not node.right:
                tmp_num = cur_num * 10 + node.val
                self.res += tmp_num
                return

            tmp_num = cur_num * 10 + node.val
            dfs(node.left, tmp_num)
            dfs(node.right, tmp_num)

        dfs(root, 0)
        return self.res 
