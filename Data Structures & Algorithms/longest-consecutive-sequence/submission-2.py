class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic_starts={}
        dic_ends={}
        for num in nums:
            if num+1 in dic_starts and num-1 not in dic_ends:
                end = dic_starts[num+1]
                del dic_starts[num+1]
                dic_starts[num]=end
                dic_ends[end]=num
            elif num-1 in dic_ends and num+1 not in dic_starts:
                start = dic_ends[num-1]
                del dic_ends[num-1]
                dic_ends[num]=start
                dic_starts[start]=num
            elif num-1 in dic_ends and num+1 in dic_starts:
                start = dic_ends[num-1]
                end = dic_starts[num+1]
                del dic_starts[num+1]
                del dic_ends[num-1]
                dic_starts[start]=end
                dic_ends[end]=start
            elif num not in dic_starts and num not in dic_ends:
                dic_starts[num]=num
                dic_ends[num]=num
            print(dic_ends)
            print(dic_starts)

        max_diff=0
        for end in dic_ends:
            start=dic_ends[end]
            max_diff=end-start+1 if end-start+1>max_diff else max_diff
        return max_diff