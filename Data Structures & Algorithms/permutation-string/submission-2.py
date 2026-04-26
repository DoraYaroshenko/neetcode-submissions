class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # dic1 = {}
        # for char in s1:
        #     dic1[char]=dic1.get(char,0)+1
        # l=0
        # for r in range(len(s1)-1,len(s2)):
        #     dic2={}
        #     for char in s2[l:r+1]:
        #         dic2[char]=dic2.get(char,0)+1
        #     if dic1!=dic2:
        #         l+=1
        #         continue
        #     return True
        # return False
        
        # dic1 = {}
        # for char in s1:
        #     dic1[char]=dic1.get(char,0)+1
        # counter=0
        # dic2={}
        # for i,char in enumerate(s2):
        #     if counter==len(s1) or dic1.get(char) is None:
        #         if dic1==dic2:
        #             return True
        #         else:
        #             counter=0
        #             dic2={}
        #     else:
        #         dic2[char]=1+dic2.get(char,0)
        #         counter+=1
        # return False

        dic1 = {}
        for char in s1:
            dic1[char]=dic1.get(char,0)+1
        counter=0
        dic2={}
        l=0
        for r in range(0, len(s2)):
            if s2[r] not in dic1:
                l=r+1
                dic2={}
                continue
            else:
                dic2[s2[r]] = 1+dic2.get(s2[r],0)
            if r-l+1 == len(s1):
                if dic1==dic2:
                    return True
                dic2[s2[l]]-=1
                l+=1
        return False