class Node:
    def __init__(self, val):
        self.prev = None
        self.nex = None
        self.val = val

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.val_freq = {} # check whether will delete the added value node
        self.val_2_node = {} # value to linked list node
        self.head = None # head of the linked list
        self.tail = None
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.head.val if self.head else -1

    def add(self, value: int) -> None:
        if value in self.val_freq:
            self.val_freq[value] += 1
        else:
            self.val_freq[value] = 1
        if self.val_freq[value] == 1:
            node = Node(value)
            if self.tail:
                self.tail.nex = node
                node.prev = self.tail
            if self.head is None:
                self.head = node
            self.tail = node
            self.val_2_node[value] = node
        else:
            if value in self.val_2_node:
                # remove value
                node = self.val_2_node[value]
                prev = node.prev
                nex = node.nex
                node.prev = None
                node.nex = None
                if prev:
                    prev.nex = nex
                else:
                    # node is the head
                    self.head = nex
                if nex:
                    nex.prev = prev
                else:
                    # node is the tail
                    self.tail = prev
                del self.val_2_node[value]
                
                


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
