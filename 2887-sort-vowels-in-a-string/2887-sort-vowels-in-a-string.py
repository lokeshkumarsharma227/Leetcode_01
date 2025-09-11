class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O','U', 'a', 'e', 'i', 'o', 'u']
        check = []
        for i in s:
            if i in vowels:
                check.append(i)
        if len(check) == 0:
            return s
        check.sort()
        s = list(s)
        count = 0
        for i in range(0, len(s)):
            if s[i] in vowels:
                s[i] = check[count]
                count += 1
        return ''.join(s)