class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        result = [0]*(len(nums))
        prod = 1
        for i in range(len(nums)):
            left.append(prod)
            prod *= nums[i]
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(prod)
            prod *= nums[i]
        right = right[::-1]
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        return result