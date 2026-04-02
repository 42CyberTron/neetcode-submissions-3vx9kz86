class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        total = 0
        res = 0
        for num in nums:
            total += num
            res += prefix_count[total-k]
            prefix_count[total] += 1
        return res