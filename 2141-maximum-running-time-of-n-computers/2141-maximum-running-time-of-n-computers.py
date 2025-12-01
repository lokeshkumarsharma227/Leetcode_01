from typing import List

class Solution:
    def isvalid(self, n, batteries: List[int], power: int) -> bool:
        need_pow= power * n
        cur_pow = 0

        for battery in batteries:
            cur_pow += min(battery, power)
            
        
        return cur_pow >= need_pow

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_energy = sum(batteries)
        min_pow = 0
        max_pow = total_energy 
        res = 0
        if(n == 1):
            return total_energy
        while min_pow < max_pow:
            power = (min_pow + max_pow) // 2

            if self.isvalid(n, batteries, power):
                res = power
                min_pow = power+1
            else:
                max_pow = power

        return res
