class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        temp = self.stack.pop()
        self.pushAll(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return self.stack
        
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
