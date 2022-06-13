class Solution:
    def hasPathSum(self, root: Optional[TreeNode], s: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and s==root.val:
            return True
        s-=root.val
        return self.hasPathSum(root.left, s) or self.hasPathSum(root.right, s)
