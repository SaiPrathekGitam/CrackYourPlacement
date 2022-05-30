class Solution:
    # ugly = sorted(2**a * 3**b * 5**c
    #               for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
    #     return self.ugly[n-1]
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]: i2 += 1
            while ugly[i3] * 3 <= ugly[-1]: i3 += 1
            while ugly[i5] * 5 <= ugly[-1]: i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]
