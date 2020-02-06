class Solution:
    def subarraySum(self, nums, target_sum) -> int:
        
        length_nums = len(nums)
        
        counter = 0
        
        for window_size in range(1, length_nums+1):
            
            sum_array = 0
            for moving_cursor in range(0, length_nums-window_size):
                
                prev_int = nums[moving_cursor]
                if moving_cursor == 0:
                    sub_array = nums[moving_cursor:moving_cursor+window_size]
                    sum_array = sum(sub_array)
                    if sum_array == target_sum:
                        counter+=1 
                else:
                    if moving_cursor+window_size < length_nums:
                        next_int = nums[moving_cursor+window_size]
                        sum_array = sum_array-prev_int+next_int
                
                        if sum_array == target_sum:
                            counter+=1        
        
        return counter