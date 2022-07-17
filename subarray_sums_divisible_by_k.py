class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        c = [1] + [0]*(k-1)
        p = 0
        res = 0
        for i in nums:
            p = (p+i)%k
            res+=c[p]
            c[p]+=1
        return res
