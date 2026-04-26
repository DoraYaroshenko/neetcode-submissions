class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        encoded_str+=f'{len(strs)}.'
        for st in strs:
            encoded_str+=f'{len(st)}.'
        for st in strs:
            encoded_str+=st
        return encoded_str

    def decode(self, s: str) -> List[str]:
        number_of_words=0
        i=0
        while s[i]!='.':
            i+=1
        number_of_words=int(s[:i])
        number_of_dots=0
        lengths_of_words=[]
        i+=1
        start_index=i
        while number_of_dots<number_of_words:
            if s[i]=='.':
                lengths_of_words.append(int(s[start_index:i]))
                start_index=i+1
                number_of_dots+=1
            i+=1
        words=[]
        for l in lengths_of_words:
            words.append(s[i:i+l])
            i=i+l
        return words


