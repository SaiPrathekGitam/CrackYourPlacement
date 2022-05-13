class Solution:
    def isHappy(self, n: int) -> bool:
        nums = [4, 16, 37, 58, 89, 145, 42, 20]
        while True:
            s = 0
            for i in str(n):
                s+=int(i)**2
            n = s
            if n==1:
                return True
            if n in nums:
                return False
