class Solution:
    def binary_search(self, left:int, right:int, target:int, nums: List[int]):
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
    
    def find_minimum(self, nums:List[int]):
        if len(nums)==1:
            return 0
        left=0
        right=len(nums)-1
        while True:
            if nums[left]<nums[right]:
                return left
            mid = (left+right)//2
            if left==right:
                return mid
            if mid>0 and nums[mid-1]>nums[mid]:
                return mid
            if mid<len(nums)-1 and nums[mid+1]<nums[mid]:
                return mid+1
            if nums[mid]<nums[left]:
                right=mid-1
            elif nums[mid]>nums[right]:
                left=mid+1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 and nums[0]!=target:
            return -1
        minimum_index = self.find_minimum(nums)
        if target<=nums[-1]:
            if target<nums[minimum_index]:
                return -1
            return self.binary_search(minimum_index, len(nums)-1,target, nums)
        else:
            if minimum_index==0:
                return -1
            return self.binary_search(0,minimum_index-1, target, nums)
        return -1
