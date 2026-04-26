class Solution:
    def isHappy(self, n: int) -> bool:
        summ=0
        s = set();
        num = n
        while num!=1:
            while num>0:
                digit=num%10
                summ+=digit**2
                num=num//10
            if summ in s:
                return False
            s.add(summ)
            num=summ
            summ=0
        return True