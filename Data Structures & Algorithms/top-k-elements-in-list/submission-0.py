class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        sorted_items = sorted(d.items(), key=lambda item:item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
