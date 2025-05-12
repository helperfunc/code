"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        tmp = p
        while tmp:
            path.add(tmp)
            tmp = tmp.parent
        
        tmp = q
        while tmp:
            if tmp in path:
                return tmp
            tmp = tmp.parent
        
        return None
        