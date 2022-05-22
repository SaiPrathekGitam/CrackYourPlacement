class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        t1 = []
        i = j = 0
        while i<len(s):
            if s1 and s[i]=='#':
                s1.pop()
            elif s[i]!='#':
                s1.append(s[i])
            i+=1
        while  j<len(t):
            if t1 and t[j]=='#':
                t1.pop()
            elif t[j]!='#':
                t1.append(t[j])
            j+=1
        return s1==t1
