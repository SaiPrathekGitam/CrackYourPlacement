class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        mw = 0
        while i<j:
            h1 = height[i]
            h2 = height[j]
            mw=max(mw, min(h1,  h2)*(j-i))
            if h1>h2:
                j-=1
            else:
                i+=1
        return mw
