# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         d = {0:0, 1:0, 2:0}
#         for i in nums:
#             d[i]+=1     
#         l =  [0]*d[0] + [1]*d[1] + [2]*d[2]
#         nums[:] = l[:]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
            if nums[i]==1:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
                i-=1
            i+=1
        return nums
