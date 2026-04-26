class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_of_subarray = 0
        max_sum=0
        if all(num<0 for num in nums):
            return max(nums)
        # [5,-10,-11,-67]
        for i,num in enumerate(nums):
            if sum_of_subarray<0:
                sum_of_subarray=0
            sum_of_subarray+=num
            max_sum=max(max_sum,sum_of_subarray)
        return max_sum