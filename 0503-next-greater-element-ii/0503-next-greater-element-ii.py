class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1]*len(nums)

        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if not stack:
                j = 0
                while nums[i] >= nums[j] and i != j:
                    j += 1

                if i != j:
                    ans[i] = nums[j]
                
                stack.append(nums[i])

            else:
                ans[i] = stack[-1]
                stack.append(nums[i])

        return ans
