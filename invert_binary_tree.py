class Solution:
    def invertTree(self, p: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(p):
            if not p:
                return
            p.left, p.right = p.right, p.left
            solve(p.right)
            solve(p.left)
            return p  
            
        solve(p)
        return p
