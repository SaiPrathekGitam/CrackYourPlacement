class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.ans
