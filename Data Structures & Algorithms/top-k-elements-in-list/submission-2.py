class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        result = []
        for num in nums:
                frequency[num]+=1  
        bucket = [[] for _ in range(len(nums)+1)]
        for i, v in frequency.items():
            bucket[v].append(i)
        for i in range(len(bucket)-1, 0, -1):
            result.extend(bucket[i])
            if len(result) == k:
                return result