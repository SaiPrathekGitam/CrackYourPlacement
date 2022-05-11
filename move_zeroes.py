class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer = 0
        i = 0
        while i<len(nums):
            if nums[i]!=0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer+=1
            i+=1
        return nums
            
