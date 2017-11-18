class MyQueue(object):
    def __init__(self):
        self.list1=[]
        self.list2=[]
    
    def peek(self):
        leng=len(self.list1)
        for ele in range(leng):
            self.list2.append(self.list1.pop())
        
        a=self.list2[leng-1]
        
        for ele in range(leng):
            self.list1.append(self.list2.pop())
            
        return a
        
    def pop(self):
        leng=len(self.list1)
        for ele in range(leng):
            self.list2.append(self.list1.pop())
        
        a=self.list2.pop()
        
        for ele in range(leng-1):
            self.list1.append(self.list2.pop())
            
        return a
        
        
    def put(self, value):
        self.list1.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        

