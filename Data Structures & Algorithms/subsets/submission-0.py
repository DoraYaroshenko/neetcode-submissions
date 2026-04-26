class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        print(f'Nums: {nums}')
        if len(nums)==0:
            return [[]]
        subsets_without_num=self.subsets(nums[1:])
        print(f'Subsets without num: {subsets_without_num}')
        lst = [x+[nums[0]] for x in subsets_without_num]
        print(f'list: {lst}')
        res+=lst+subsets_without_num
        print(f'Res: {res}')
        return res