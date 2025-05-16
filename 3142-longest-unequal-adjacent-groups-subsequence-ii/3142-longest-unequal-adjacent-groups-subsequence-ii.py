class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp=[1]*(len(words))
        store=[-1]*len(words)
        for i in range(len(words)-1,-1,-1):
            for j in range(i+1,len(words)):
                hammingdistance = 0
                if len(words[i])==len(words[j]):
                    for k in range(len(words[i])):
                        if words[i][k]!=words[j][k]:
                            hammingdistance+=1
                if hammingdistance==1 and groups[i]!=groups[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        store[i]=j
        maxi = max(dp)
        idx = dp.index(maxi)
        res = [words[idx]]
        while maxi!=1:
            res.append(words[store[idx]])
            idx=store[idx]
            maxi -= 1
        return res