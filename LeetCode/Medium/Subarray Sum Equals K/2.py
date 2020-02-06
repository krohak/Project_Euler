class Solution:
    def subarraySum(self, nums: List[int], target_sum: int) -> int:
        
        length_nums = len(nums)
        
        counter = 0

        for window_size in range(0, length_nums):
            
            prev_start_num = 0
            curr_sum = 0
            
            for start in range(0, length_nums-window_size):
                    
                if start==0:
                    curr_sum = sum(nums[start:start+window_size+1])
                    
                else:
                    this_next_num = nums[start+window_size]
                    curr_sum = curr_sum + this_next_num - prev_start_num
                
                if curr_sum == target_sum:
                    counter+=1
                    
                prev_start_num = nums[start]
                    
        return counter