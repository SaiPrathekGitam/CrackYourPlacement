class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = m = 0
        for i in s:
            if i=='(':
                c+=1
                m = max(m, c)
            elif i==')':
                c-=1
        return m
                
