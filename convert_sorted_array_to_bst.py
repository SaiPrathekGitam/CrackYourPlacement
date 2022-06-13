class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums, left, right):
            if left==right:
                return None
            mid = (left+right)//2
            node = TreeNode(nums[mid])
            node.left = dfs(nums, left, mid)
            node.right = dfs(nums, mid+1, right)
            return node
        return dfs(nums, 0, len(nums))
