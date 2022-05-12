class Solution:
    def strStr(self, haystack, needle):
        def kmp(needle):
            i = 1
            j = 0
            
            res = [0] * len(needle)
            while i < len(needle):
                if needle[i] == needle[j]:
                    res[i] = j + 1
                    i += 1
                    j += 1
                elif j > 0:
                    j = res[j-1]
                else:
                    res[i] = 0
                    i += 1
                    
                    
            return res
        
        if haystack == [] or needle == [] or len(needle) > len(haystack):
            return -1
        
        pattern = kmp(needle)
        
        i = j = 0
        while i < len(haystack) and j < len(needle):

            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j-1]
            else:
                i += 1
                
                
        if j == len(needle):
            return i - j
        else:
            return -1
