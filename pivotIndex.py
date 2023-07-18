class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        sum_i = 0
        t = 0
        for i in nums: 
            sum_i = sum_i + i
        for i in range(0,len(nums)):
            sum_i = sum_i - nums[i] 
            if(sum_i == t):
                return i
            t = t + nums[i]
        return -1