from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for nums, freq in count.items():
            heapq.heappush(heap, (freq, nums))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]     