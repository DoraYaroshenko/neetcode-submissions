class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            if num in dic.keys():
                dic[num]+=1
            else:
                dic[num]=0
        dic2={}
        for key,value in dic.items():
            if value in dic2.keys():
                dic2[value].append(key)
            else:
                dic2[value] = [key]
        k_most = []
        while len(k_most)<k:
            k_most+=(dic2[max(dic2.keys())][:k])
            del dic2[max(dic2.keys())]
        return k_most