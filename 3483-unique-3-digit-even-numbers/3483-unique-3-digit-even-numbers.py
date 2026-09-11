class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()
        digit_count = Counter(digits)
        
        for first in digit_count:
            if first == 0:
                continue
            digit_count[first] -= 1
            
            for second in digit_count:
                if digit_count[second] == 0:
                    continue
                digit_count[second] -= 1
                
                for last in digit_count:
                    if digit_count[last] > 0 and last % 2 == 0:
                        num = first * 100 + second * 10 + last
                        nums.add(num)
                
                digit_count[second] += 1
            
            digit_count[first] += 1
        
        return len(nums)