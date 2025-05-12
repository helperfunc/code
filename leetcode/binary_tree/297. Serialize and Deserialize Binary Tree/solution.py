# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        1 2 null null 3 4 5
        """
        res = []
        def preorder(node):
            if not node:
                res.append('null')
                return 
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ' '.join(res)
 
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(' ')
        self.ind = 0
        def cal():
            if res[self.ind] == 'null':
                self.ind += 1
                return None
            root = TreeNode(res[self.ind])
            self.ind += 1
            root.left = cal()
            root.right = cal()
            return root

        return cal()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
