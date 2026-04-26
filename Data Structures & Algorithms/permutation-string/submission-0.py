class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        for char in s1:
            dic1[char]=dic1.get(char,0)+1
        l=0
        for r in range(len(s1)-1,len(s2)):
            dic2={}
            for char in s2[l:r+1]:
                dic2[char]=dic2.get(char,0)+1
            if dic1!=dic2:
                l+=1
                continue
            return True
        return False
            