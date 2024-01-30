# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # level, height
        # level_height_node_val[level] = [(height, node_val)] # heap, maxheap
        node_level = {}
        node_height = {}
        level_height_node_val = collections.defaultdict(list)
        def dfs(node, level):
            if not node:
                return 0
            left_height = dfs(node.left, level + 1)
            right_height = dfs(node.right, level + 1)
            height = max(left_height, right_height) + 1
            node_level[node.val] = level
            node_height[node.val] = height
            level_height_node_val[level].append((height, node.val))
            return height

        height_tree = dfs(root, 0)
        
        for l, height_node_vals in level_height_node_val.items():
            height_node_vals.sort(reverse=True)
            # number at level * log (number at level) + log(number at level)
            
        res = []
        for q in queries:
            l = node_level[q]
            h = node_height[q]
            if h == level_height_node_val[l][0][0]:
                # this node is with the maximum height of the level
                if len(level_height_node_val[l]) == 1:
                    res.append(height_tree - h - 1)
                else:
                    res.append(height_tree - (h - level_height_node_val[l][1][0]) - 1)
            else:
                res.append(height_tree - 1)
        return res
