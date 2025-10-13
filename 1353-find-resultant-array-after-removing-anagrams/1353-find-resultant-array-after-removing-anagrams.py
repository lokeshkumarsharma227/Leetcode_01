class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        answer = [words[0]]
        for word in words[1:]:
            if sorted(word) != sorted(answer[-1]):
                answer.append(word)
        return answer