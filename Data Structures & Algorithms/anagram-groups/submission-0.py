class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sorted_s = ''.join(sorted(s));
            if dic.get(sorted_s) is None:
                dic.update({sorted_s: []});
            arr = dic[sorted_s]
            arr.append(s)
        return dic.values()