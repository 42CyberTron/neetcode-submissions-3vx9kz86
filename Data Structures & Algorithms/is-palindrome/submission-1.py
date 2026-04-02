class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        palid = ""
        palid = s[::-1]
        if s == palid:
            return True
        return False