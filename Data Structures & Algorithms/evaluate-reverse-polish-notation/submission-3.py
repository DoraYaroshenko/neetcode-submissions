import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            res=0
            if char in ('+','-','*','/'):
                arg1=stack.pop()
                arg2=stack.pop()
                print(f"arg1: {arg1}, arg2: {arg2},")
                match char:
                    case '+':
                        res=arg1+arg2
                    case '-':
                        res=arg2-arg1
                    case '*':
                        res=arg1*arg2
                    case '/':
                        res=int(arg2/arg1)
            else:
                res=int(char)
            stack.append(res)
            print(f"Char: {char}, res: {res}, stack: {stack}")
        return stack[-1]