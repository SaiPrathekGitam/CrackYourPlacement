class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        i = columnNumber
        ans = ''
        while i>0:
            ans+=chr(((i-1)%26)+65)
            i=(i-1)//26 
        return ans[::-1]      
            
