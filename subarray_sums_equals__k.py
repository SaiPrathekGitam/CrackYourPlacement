class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = {0:1}
        p = 0
        res = 0
        for i in nums:
            p = p+i
            temp = p-k
            if temp in c:
                res+=c[temp]
            if p in c:
                c[p]+=1
            else:
                c[p]=1
           
        return res
