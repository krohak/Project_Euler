class Solution:
    def generate(self, numRows):
        
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        
        answers = []
        
        answers.append([1])
        
        ans_prev = [1,1]
        answers.append(ans_prev)
        
        for _ in range(numRows-2):
            len_ans_prev = len(ans_prev)
            
            ans = []
            ans.append(1)
            
            for i in range(1, len_ans_prev):
                ans.append(ans_prev[i-1] + ans_prev[i])
            ans.append(1)
            
            answers.append(ans)
            ans_prev = ans
        
        return answers
            