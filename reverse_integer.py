class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            ans = int(str(x)[::-1])
        else:
            ans = -int(str(x)[:0:-1])
        if -2147483648<=ans<2147483648:
            return ans 
        return 0
