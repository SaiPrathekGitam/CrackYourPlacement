class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        mon = []
        numsIndex = {n:i for i, n in enumerate(nums1)}
        ret = [-1]*len(nums1)
        for i in nums2:
            while mon and i>mon[-1]:
                ret[numsIndex[mon.pop()]] = i
            if i in nums1:
                mon.append(i)

        return ret
