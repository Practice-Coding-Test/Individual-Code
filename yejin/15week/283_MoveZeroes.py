class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointers
        ps = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ps], nums[i] = nums[i], nums[ps]
                ps += 1