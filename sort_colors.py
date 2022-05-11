class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = {0:0, 1:0, 2:0}
        for i in nums:
            d[i]+=1     
        l =  [0]*d[0] + [1]*d[1] + [2]*d[2]
        nums[:] = l[:]
