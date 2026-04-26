class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        while True:
            if nums[left]<nums[right]:
                return nums[left]
            mid = (left+right)//2
            if left==right:
                return nums[mid]
            if mid>0 and nums[mid-1]>nums[mid]:
                return nums[mid]
            if mid<len(nums)-1 and nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if nums[mid]<nums[left]:
                right=mid-1
            elif nums[mid]>nums[right]:
                left=mid+1