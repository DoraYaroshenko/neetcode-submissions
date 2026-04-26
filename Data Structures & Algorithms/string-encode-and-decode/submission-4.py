class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            len_s = str(len(s))
            padding = (str(0)*(203-len(s)-len(len_s)))
            res+=(s+padding+len_s)
        return res

    def decode(self, s: str) -> List[str]:
        arr = []
        i=200
        j=0
        while i<len(s):
            len_s = int(s[i:i+3])
            arr.append(s[j:len_s+j])
            i+=203
            j+=203
        return arr
