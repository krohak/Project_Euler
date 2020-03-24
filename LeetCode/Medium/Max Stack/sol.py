class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.max_stack:
            self.max_stack.append(max(self.max_stack[-1], x))
        else:
            self.max_stack.append(x)
        

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
        
    def peekMax(self) -> int:
        return self.max_stack[-1]
        
        
    def popMax(self) -> int:
        max_elem = self.max_stack.pop()
        index = len(self.stack)-1
        for elem in reversed(self.stack):
            if elem == max_elem:
                break
            index-=1
        
        old_slice = self.stack[:index]
        new_slice = self.stack[index+1:]
        
        old_max = self.max_stack[:index]
        
        for elem in new_slice:
            old_slice.append(elem)
            if not old_max:
                old_max.append(elem)
            else:
                old_max.append(max(old_max[-1], elem))
        
        self.stack =  old_slice
        self.max_stack = old_max
        return max_elem
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()