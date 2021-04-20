class Solution:
    def wordsTyping(self, sentence: list, rows: int, cols: int) -> int:
        sentenceLen  = len(sentence)
        dp = [ 0 for _ in range(sentenceLen)]
        
        for i in range(sentenceLen):
            
            j = (i + 1) % sentenceLen
            numChars = len(sentence[i])
            words = 1
            
            if len(sentence[j]) > cols:
                return 0
            
            while numChars + 1 + len(sentence[j]) <= cols:
                numChars += (len(sentence[j]) + 1)
                j = (j+1) % sentenceLen
                words += 1
            
            dp[i] = words
        
        totalWords = 0
        i = 0
        while rows:
            totalWords += dp[i]
            i = (dp[i] + i) % sentenceLen
            rows-=1
            
        print(dp, totalWords, sentenceLen)
        return totalWords // sentenceLen
        