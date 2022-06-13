class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(i, path):
            if not i.left and not i.right:
                res.append('->'.join(path+[str(i.val)]))
            if i.right:
                dfs(i.right, path+[str(i.val)])
            if i.left:
                dfs(i.left,  path+[str(i.val)])
        dfs(root, [])
        return res
