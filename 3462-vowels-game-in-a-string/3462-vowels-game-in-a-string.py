class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = 'aeiouAEIOU'
        for i in vowel:
            if i in s:
                return True
        else:
            return False