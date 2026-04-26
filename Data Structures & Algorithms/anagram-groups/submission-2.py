class Solution:
    def build_representation(self, s: str) -> str:
        s_counter=[0]*26
        st=""
        for char in s:
            s_counter[ord(char)-97]+=1
        for count in range(26):
            st+=f'{chr(count+97)}{s_counter[count]}'
        return st
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for st in strs:
            # sorted_st = "".join(sorted(st))
            # if sorted_st in dic.keys():
            #     dic[sorted_st].append(st)
            # else:
            #     dic[sorted_st]=[st]
            st_rep = self.build_representation(st)
            if st_rep in dic.keys():
                dic[st_rep].append(st)
            else:
                dic[st_rep]=[st]
        return list(dic.values())
