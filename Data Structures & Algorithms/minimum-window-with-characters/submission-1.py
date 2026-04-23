from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        for char in t:
            count[char] += 1
        
        for window_size in range(len(t), len(s) + 1):
            left, right = 0, window_size
            current_window = defaultdict(int)
            for char in s[0:window_size]:
                current_window[char] += 1
            if all(current_window[c] >= count[c] for c in count):
                return s[left:right]
            while right < len(s):
                current_window[s[left]] -= 1
                current_window[s[right]] += 1
                left += 1
                right += 1
                if all(current_window[c] >= count[c] for c in count):
                    return s[left:right]
        
        return ""