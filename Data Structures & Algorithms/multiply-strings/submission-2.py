class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        for i in range(len(num1)):
            n1+=int(num1[len(num1)-i-1])*(10**i)
        for i in range(len(num2)):
            n2+=int(num2[len(num2)-i-1])*(10**i)
        print(n1)
        print(n2)
        return str(n1*n2)