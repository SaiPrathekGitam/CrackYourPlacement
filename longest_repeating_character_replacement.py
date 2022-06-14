class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        m = l = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]]+=1
            else:
                count[s[r]]=1
            m = max(m, count[s[r]])
            if r-l+1-m>k:
                count[s[l]]-=1
                l+=1
        return len(s)-l
