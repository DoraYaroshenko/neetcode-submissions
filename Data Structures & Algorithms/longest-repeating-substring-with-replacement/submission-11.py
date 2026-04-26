class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        # dic_of_appearences = {}
        # start=0
        # end=0
        # appearences_of_most_frequent=0
        # most_frequent='a'
        # max_len=1
        # for char in s:
        #     if dic_of_appearences.get(char) is None:
        #         dic_of_appearences[char]=1
        #     else:
        #         dic_of_appearences[char]+=1
        # for key in dic_of_appearences:
        #     if dic_of_appearences[key]>appearences_of_most_frequent:
        #         appearences_of_most_frequent=dic_of_appearences[key]
        #         most_frequent=key
        # print(most_frequent)
        # num_of_chars_to_replace = 0
        # index_of_first_to_replace=0
        # met_to_replace=False
        # for i,char in enumerate(s):
        #     end=i
        #     print(s[start:end+1])
        #     if char!=most_frequent:
        #         num_of_chars_to_replace+=1
        #         if met_to_replace==False:
        #             index_of_first_to_replace=i
        #             print("!", index_of_first_to_replace)
        #             met_to_replace=True
        #         if num_of_chars_to_replace>k:
        #             start=index_of_first_to_replace+1
        #             # met_to_replace=False
        #             index_of_first_to_replace+=1
        #     if end-start+1>max_len:
        #         max_len=end-start+1
        #     print(max_len)
        count = {}
        maxf=0
        l=0
        max_len=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxf = max(count[s[r]], maxf)
            while r-l+1 - maxf>k:
                count[s[l]]-=1
                l+=1
            max_len = max(max_len,r-l+1)
        return max_len

            