class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = collections.Counter(nums)
        # return sorted(dic, key = dic.get,reverse = True)[:k]
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        heap = []
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key], key))
        res = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        
        return res
