class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []

        for key in counts:
            heapq.heappush(heap, (counts[key], key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [tup[1] for tup in heap]
            



