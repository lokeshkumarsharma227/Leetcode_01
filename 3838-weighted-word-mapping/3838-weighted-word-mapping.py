class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""

        for i in words:
            all=0
            for j in i:
                all+=weights[ord(j)-ord('a')]

            out=all%26
            ans+=chr(ord('z')-out)

        return ans