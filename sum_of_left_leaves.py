class Solution:
    ans = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val if isLeft else 0    
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)
