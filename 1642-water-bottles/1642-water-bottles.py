class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
	
        def helper(full, empty, drank):
            if full + empty < numExchange:
                return drank+full
            if full:
                empty += full
            new = empty // numExchange
            remaining_empt = empty - (new*numExchange)
            return helper(new, remaining_empt, drank + full)
            
        return helper(numBottles, 0, 0)