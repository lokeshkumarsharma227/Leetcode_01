class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        res = 0
        unq = {}
        for right, ftype in enumerate(fruits):
            if len(unq)<2:
                if ftype not in unq:
                    unq[ftype] = 0
                unq[ftype]+=1
                continue
            if ftype not in unq:
                res = max(res, right-left)
                unq[ftype] = 0
                unq[ftype]+=1
                while left<=right and len(unq)>2:
                    unq[fruits[left]]-=1
                    if unq[fruits[left]]==0:
                        del unq[fruits[left]]
                    left+=1
            else:
                unq[ftype]+=1
        res = max(res, right-left+1)
        return res
