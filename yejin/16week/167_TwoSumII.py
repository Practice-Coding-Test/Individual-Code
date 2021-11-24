class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l, r = 0, len(numbers) - 1
        # while l <= r:
        #     if numbers[l] + numbers[r] == target: return [l+1, r+1]
        #     elif numbers[l] + numbers[r] > target: r -=1
        #     else: l += 1
        # 76ms
        d = {}
        
        for i, n in enumerate(numbers):
            if target - n in d:
                return  d[target-n]+1,i+1
            else:
                d[n] = i