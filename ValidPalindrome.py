class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 0):
            return True
        s = s.lower()
        slist = [char for char in s if char.isalnum()]
        sstack = slist
        for char in slist:
            if(char != sstack.pop()):
                return False
        return True
