class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            return False
        return dfs(root.left, root.right)
