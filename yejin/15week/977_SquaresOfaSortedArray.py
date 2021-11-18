class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [i*i for i in sorted(nums,key=lambda x:abs(x))]