class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        windows = []
        for i in range(0, len(nums)):
            windows.append(nums[i])
            if len(windows) == k:
                res.append(max(windows))
                windows.pop(0)
        return res