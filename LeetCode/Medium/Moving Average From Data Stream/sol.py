from collections import deque
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.counter = 0
        self.average = 0
        self.dll = deque()

    def next(self, val):
        
        if self.counter < self.size:
            self.average = ((self.average*self.counter)+val)/(self.counter+1)
            self.dll.append(val)
            self.counter+=1
        
        else:
            previous_data = self.dll.popleft()
            self.dll.append(val)
            self.average = ((self.average*self.size)-previous_data+val)/(self.size)
            
        return self.average
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)