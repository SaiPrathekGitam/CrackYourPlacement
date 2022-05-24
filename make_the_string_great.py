class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            
            if stack and stack[-1].isupper() ^ i.isupper() and stack[-1].upper() == i.upper():
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
