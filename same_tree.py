class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def solve(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val==q.val) and solve(p.left, q.left) and solve(p.right, q.right)
        return solve(p, q)
