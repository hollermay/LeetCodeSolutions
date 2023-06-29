class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = len(nums)
        for i in nums[:]:
            if i == val:
                nums.remove(val)
        return len(nums)
