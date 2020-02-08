from collections import Counter

class Solution:
    def threeSum(self, arr):
        
        length_arr = len(arr)

        used_triplets = set()
        freq_dict = Counter(arr)
        
        answers = []
        
        i = 0 
        while i < length_arr:
            j = i+1
            while j < length_arr:
                
                freq_dict[arr[i]] -= 1
                freq_dict[arr[j]] -= 1
                
                remaining = 0 - arr[i] - arr[j]
                
                if remaining in freq_dict and freq_dict[remaining] > 0:
                    if not (arr[i], arr[j]) in used_triplets and not (arr[j], arr[i]) in used_triplets:
                        answers.append([arr[i], arr[j], remaining])
                        used_triplets.add((arr[i],arr[j]))
                        used_triplets.add((arr[i],remaining))
                        used_triplets.add((arr[j],remaining))
                
                freq_dict[arr[i]] += 1
                freq_dict[arr[j]] += 1
            
                j+=1
            
            i+=1
        
        return answers
                
            