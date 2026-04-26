class MinStack:

    def __init__(self):
        self.lst = []
        self.minlst = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        if len(self.minlst)==0:
            self.minlst.append(val)
        else:
            if val<=self.minlst[-1]:
                self.minlst.append(val)

    def pop(self) -> None:
        top = self.lst.pop()
        if top==self.minlst[-1]:
            self.minlst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minlst[-1]
