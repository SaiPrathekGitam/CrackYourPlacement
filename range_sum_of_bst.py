class Solution:
    ans = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return
            if low<=root.val<=high:
                self.ans+=root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans
