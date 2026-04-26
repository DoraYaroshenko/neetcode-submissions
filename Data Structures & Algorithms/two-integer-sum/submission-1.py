class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i in range(len(nums)):
            if target-nums[i] in nums_set:
                for j in range(i+1,len(nums)):
                    if nums[j]==target-nums[i]: return [i,j]