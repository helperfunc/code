# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vert_order = collections.defaultdict(list)

        # def pre_order(node, col):
        #     if not node:
        #         return
        #     vert_order[col].append(node.val)
        #     pre_order(node.left, col - 1)
        #     pre_order(node.right, col + 1)
        def level_order():
            q = collections.deque([(root, 0)])
            while q:
                for _ in range(len(q)):
                    node, col = q.popleft()
                    vert_order[col].append(node.val)
                    if node.left:
                        q.append((node.left, col - 1))
                    if node.right:
                        q.append((node.right, col + 1))
        
        # pre_order(root, 0)
        if not root:
            return []
        level_order()
        res = [None] * len(vert_order)
        tmp_min = min(vert_order.keys())
        for k, l in vert_order.items():
            res[k - tmp_min] = l
        return res