class Node():
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.fow = None
        self.back = None
        

class LRUCache(object):
    
    
    def move_end(self, node):
        if self.dll_end:
            
            node.back.fow = node.fow.back
            
            self.dll_end.fow = node
            node.back = self.dll_end.fow
        else:
            self.dll_end = node
            self.dll_start.fow = self.dll_end
            self.dll_end.back = self.dll_start
    
    def remove_start(self):
        
        if self.dll_start.key in self.cache:
            del self.cache[self.dll_start.key]
        
            self.dll_start = self.dll_start.fow
        
            self.size-=1
        
        return 
        

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dll_start = None
        self.dll_end = None
        self.cache = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        to_return = -1
        if key in self.cache:
            to_return = self.cache[key].value
            self.move_end(self.cache[key])
        
        return to_return
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key].value = value
            self.move_end(self.cache[key])
            return 
        
        if not self.dll_start:
            self.cache[key] = Node(key, value)
            self.dll_start = self.cache[key]
            self.size+=1
            
            self.dll_start.fow = self.dll_start
            self.dll_start.back = self.dll_start
            return
            
        self.cache[key] = Node(key, value)
        self.size+=1
        self.move_end(self.cache[key])
        
        if self.size > self.capacity:
            self.remove_start()
        return 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)