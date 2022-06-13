class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(depth, root):
            if not root:
                return depth
            return max(dfs(depth+1, root.left), dfs(depth+1, root.right))
            
        return dfs(0, root)
