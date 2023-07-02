class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li =[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    li.append(nums1[i])
        res = [*set(li)]
        return res
