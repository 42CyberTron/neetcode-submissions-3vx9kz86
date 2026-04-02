class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        current_streak = 1
        max_streak = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i]+1 == nums[i+1]:
                current_streak += 1
            else:
                current_streak = 1
            max_streak = max(current_streak, max_streak)
        return max_streak