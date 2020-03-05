from collections import defaultdict
import heapq

class min_heap:

    def __init__(self):
        self.cur_size = 0
        self.heap = []

    def add_new(self, elem):

        if self.cur_size < 5:
            heapq.heappush(self.heap, elem)
            self.cur_size+=1

        else:
            if self.heap[0] < elem:
                heapq.heappushpop(self.heap, elem)

class Solution:
                
    def highFive(self, items):
        
        student_highs = defaultdict(min_heap)
        
        for student_id, score in items:
            student_highs[student_id].add_new(score)
        
        ans = []
        for student_id, heapobj in student_highs.items():
            avg = sum(heapobj.heap)//5
            ans.append([student_id, avg])
            
        return ans