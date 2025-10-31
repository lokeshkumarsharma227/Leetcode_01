class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited=set()
        sneaky_nums=[]
        for num in nums:
            if num in visited:
                sneaky_nums.append(num)
            else:
                visited.add(num)
        return sneaky_nums