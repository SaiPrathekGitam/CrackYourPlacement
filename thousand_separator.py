class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<1000:
            return str(n)
        n = str(n)
        stack = n[0]
        for i in range(1, len(n)):
            if (len(n)-i)%3==0:
                stack+='.'
            stack+=n[i]
        return stack
