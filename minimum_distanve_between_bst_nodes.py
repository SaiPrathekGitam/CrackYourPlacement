class Solution:
    res = 100000
    pre = -100000
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            self.res = min(self.res, root.val-self.pre)
            self.pre = root.val
            dfs(root.right)
        dfs(root)
        return self.res
