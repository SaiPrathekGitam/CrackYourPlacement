class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_ = '({['
        close_ = ')}]'
        for i in s:
            if i in close_ and len(stack)!= 0 and stack[-1] == open_[close_.index(i)]:
                stack.pop()
            elif i in open_:
                stack.append(i)
            else:
                return False
        if len(stack)==0:
            return True
        return False
    
