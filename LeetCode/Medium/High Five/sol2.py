from collections import defaultdict
import heapq

class Solution:
                
    def highFive(self, items):
        
        student_highs = defaultdict(list)
        
        for student_id, score in items:
            student_highs[student_id].append(-score)
        
        ans = []
        for student_id, student_heap in student_highs.items():
            heapq.heapify(student_heap)
            high_five = 0
            for _ in range(5):
                high_five-=heapq.heappop(student_heap)
            ans.append([student_id, high_five//5])
            
        return ans