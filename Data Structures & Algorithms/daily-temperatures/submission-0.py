class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack=[]
        temp_stack.append(0)
        res=[0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while temp_stack and temperatures[i]>temperatures[temp_stack[-1]]:
                # print(f'Last index in stack: {temp_stack[-1]}, last temp in stack: {temperatures[temp_stack[-1]]}, i: {i}, temp: {temperatures[i]}')
                res[temp_stack[-1]]=i-temp_stack[-1]
                temp_stack.pop()
            temp_stack.append(i)
        return res

