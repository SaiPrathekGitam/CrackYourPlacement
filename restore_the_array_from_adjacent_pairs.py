class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = {}
        for i in adjacentPairs:
            for j in range(2):
                if i[j] in d:
                    d[i[j]].append(i[2-j-1])
                else:
                    d[i[j]] = [i[2-j-1]]
        for i in d:
            if len(d[i])==1:
                res = [i]
                break
        res+=d[res[-1]]
        while True:
            if len(d[res[-1]])==1:
                return res
            for i in d[res[-1]]:
                if i!=res[-2]:
                    res.append(i)
                    break
                    
