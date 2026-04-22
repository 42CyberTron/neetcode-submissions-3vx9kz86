class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            seen = set()
            res = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    res += 1
            longest = max(longest, res)
        return longest
        