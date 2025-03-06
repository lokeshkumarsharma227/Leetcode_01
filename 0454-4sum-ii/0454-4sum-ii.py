class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hp = {}
        count = 0

        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                if s in hp:
                    hp[s] += 1
                else:
                    hp[s] = 1

        for n3 in nums3:
            for n4 in nums4:
                target = -(n3 + n4)
                if target in hp:
                    count += hp[target]

        return count

        