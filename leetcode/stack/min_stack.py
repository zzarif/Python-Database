class MinStack:

    def __init__(self):
        self.minStack = []
        # min() requires O(n) runtime
        # that's why keeping track of minimums
        self.minimums = []


    def push(self, val: int) -> None:
        self.minStack.append(val)
        latest_min = min(val, self.minimums[-1] if self.minimums else val)
        self.minimums.append(latest_min)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.minimums.pop()
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        # min() requires O(n) runtime
        # return min(self.minStack)

        # returning latest minimum is O(1)
        return self.minimums[-1]