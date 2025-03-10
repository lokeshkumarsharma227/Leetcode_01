class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        mp = defaultdict(int)
        ans = 0

        for i in answers:
            if mp[i] == 0:  
                ans += i + 1  
                mp[i] = i  
            else:
                mp[i] -= 1  

        return ans
