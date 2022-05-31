class Solution:
    def reorganizeString(self, S):   
        if not S:
            return ""
        d = {}
        for c in S:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        h = []
        from heapq import heappush, heappop
        for k in d:
            heappush(h, (-d[k], k))

        res = []
        while len(h) > 1:
            f1, c1 = heappop(h)
            f2, c2 = heappop(h)

            res.append(c1)
            res.append(c2)

            if abs(f1) > 1:
                heappush(h, (f1+1, c1))
            if abs(f2) > 1: 
                heappush(h, (f2+1, c2))

        if h:
            f, c = h[0]
            if abs(f) > 1: 
                return "" 
            else:
                res.append(c)
        return ''.join(res) 
