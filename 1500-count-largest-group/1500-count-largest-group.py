class Solution:
    def countLargestGroup(self, n: int) -> int:
        l = [[] for _ in range(37)]
        for i in range(1, n + 1):
            s = sum(int(d) for d in str(i)) 
            l[s].append(i)
        max_length = max(len(sublist) for sublist in l)
        count = 0 
        for i in l:
            if (len(i) == max_length):
                count += 1
            else:
                pass
        return count