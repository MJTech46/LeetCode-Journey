from string import punctuation

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join([char if char not in punctuation+" " else "" for char in s]).lower()
        return True if s==s[::-1] else False