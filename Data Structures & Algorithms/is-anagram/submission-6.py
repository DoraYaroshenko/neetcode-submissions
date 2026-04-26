class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = "".join(sorted(s))
        # sorted_t = "".join(sorted(t))
        # return sorted_s==sorted_t
        s_counter = [0]*26
        t_counter=[0]*26
        for char in s:
            s_counter[ord(char)-97]+=1
        for char in t:
            t_counter[ord(char)-97]+=1
        for count in range(26):
            if s_counter[count]!=t_counter[count]:
                return False
        return True