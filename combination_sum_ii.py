class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, path, target):
            if target==0:
                return res.append(path)        
            for j in range(i, len(candidates)):
                if j!=i and candidates[j-1] == candidates[j]:
                    continue
                if target-candidates[j]<0:
                    break
                dfs(j+1, path+[candidates[j]], target-candidates[j])
        dfs(0, [], target)
        return res
