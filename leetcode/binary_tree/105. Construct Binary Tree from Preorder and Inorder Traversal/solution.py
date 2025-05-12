# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # recursive 
        # length of the left tree -> get the preorder and inorder of the left tree and right tree
        # #           l1        r1
        # preorder = [3,9,20,15,7]
        # #          l2         r2
        # inorder = [9,3,15,20,7]
                    #  i
        def build(l1, r1, l2, r2):
            if l1 > r1 or l2 > r2:
                return None
            root = TreeNode(preorder[l1])
            i = l2
            while inorder[i] != preorder[l1]:
                i += 1
            root.left = build(l1 + 1, l1 + i - l2, l2, i - 1)
            root.right = build(l1 + i - l2 + 1, r1, i + 1, r2)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

