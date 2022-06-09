class Solution:
    def combine(self, nums: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        def bt(start):
            if len(comb)==k:
                res.append(comb.copy())
                return 
            for i in range(start, nums+1):
                comb.append(i)
                bt(i+1)
                comb.pop()
                
        bt(1)
        return res  
                
