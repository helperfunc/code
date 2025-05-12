"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class WrapperInt:
    def __init__(self,val):
        self.val = val
    def get(self):
        return self.val
    def incr(self):
        self.val += 1

class Codec:
    def dfs_serialize(self, node, serialized_list):
        if not node:
            return 
        serialized_list.append(chr(node.val+48)) # unicode '0' 48   ord(chr(node.val)) is not the digit character ord(chr(node.val)) == '#'
        for child in node.children:
            self.dfs_serialize(child, serialized_list)
        serialized_list.append('#')
        
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        # 1 3 5 # 6 # # 2 # 4 # #
        # 135 -> 13 5 -> 1 3 5 -> 1 35 -> unicode
        serialized_list = []
        self.dfs_serialize(root, serialized_list)
        return ''.join(serialized_list)
	
    def dfs_deserialize(self, data, ind):
        if ind.get() == len(data):
            return
        n = Node(ord(data[ind.get()]) - 48)
        ind.incr()
        while data[ind.get()] != '#':
            n.children.append(self.dfs_deserialize(data, ind))
        ind.incr()
        return n

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        ind = WrapperInt(0) # if we use integer, the recursive call of self.dfs_deserialize(data, ind) will lost the increased ind
        return self.dfs_deserialize(data, ind)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
