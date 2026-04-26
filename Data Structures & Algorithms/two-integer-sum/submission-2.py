class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookfor_indice={}
        for i,num in enumerate(nums):
            if num in lookfor_indice.keys():
                return [lookfor_indice[num],i]
            lookfor_indice[target-num]=i