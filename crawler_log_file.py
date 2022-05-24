class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = 0
        for i in logs:
            if i[:2] == '..' and stack!=0:
                stack-=1
            elif i[0] != '.':
                stack+=1
        return stack
