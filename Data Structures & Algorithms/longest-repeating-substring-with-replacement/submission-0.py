class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}
        left, right = 0, 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            window_size = right - left + 1
            if window_size - max(count.values()) > k:
                count[s[left]]-=1
                left += 1
            longest = max(longest, (right-left+1))
        return longest