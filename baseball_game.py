class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if i == '+':
                stack.append(stack[-1]+stack[-2])
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
                
        
