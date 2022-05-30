class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        for i in nums[k:]:
            heapq.heappushpop(pq, i)
        return pq[0]
