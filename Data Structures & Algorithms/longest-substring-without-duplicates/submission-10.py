class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        dic = {}
        window = set()
        start=0
        end=0
        counter=0
        max_len_of_substring = 1
        for i,char in enumerate(s):
            end=i
            # print(start,end, counter, dic.get(char))
            if char not in window:
                counter+=1
                window.add(char)
            else:
                start = dic[char]+1
                # print(start,end)
                window = set(s[start:end+1])
                # print("!",window,"!")
                counter = end-start+1
            if counter>max_len_of_substring:
                max_len_of_substring=counter
            dic[char] = i
        return max_len_of_substring