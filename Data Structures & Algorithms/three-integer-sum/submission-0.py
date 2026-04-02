class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            j = nums[i]
            while left < right:
                curr = nums[left] + nums[right]
                if curr == -j:
                    result.append([j, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                if curr > -j:
                    right -= 1
                if curr < -j:
                    left += 1
        return result                  