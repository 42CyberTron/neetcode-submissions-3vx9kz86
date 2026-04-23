class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windows_size = len(s1)
        left, right = 0, 0
        count_s1 = {}
        count_window = {}
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1
        for right in range(len(s2)):
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1
            if right - left + 1 > windows_size:
                count_window[s2[left]] -= 1
                if count_window[s2[left]] == 0:
                    del count_window[s2[left]]
                left += 1
            if count_s1 == count_window:
                return True
        return False