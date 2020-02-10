class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        word_to_freq = {}
        freq_to_word = {}
        
        for word in words:
            if word in word_to_freq:
                word_to_freq[word]+=1
            else:
                word_to_freq[word] = 1
        
        for word, freq in word_to_freq.items():
            if freq in freq_to_word:
                freq_to_word[freq].append(word)
            else:
                freq_to_word[freq] = []
                freq_to_word[freq].append(word)
                
        answer = []
        for i in range(len(words), 0, -1):
            
            if i in freq_to_word:
                freq_to_word[i].sort()
                for alphabetical_word in freq_to_word[i]:
                    answer.append(alphabetical_word)
        
        if k <= len(answer):
            return answer[:k]
        
        return answer
                    
            