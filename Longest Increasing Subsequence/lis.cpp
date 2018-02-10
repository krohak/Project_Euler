class Solution {
public:
    
    int counter;
    
    int smallest_in_left(const vector<int>& nums, int l, int r){
        
        
        
        if ( l == r ){
            //counter = 1;
            return nums[l];
        }
        
        int mid = (l+r)/2;
        
        int left_small = smallest_in_left(nums,l,mid);
        int right_small = smallest_in_left(nums,mid+1,r);
        
       /* if ( left_small == numeric_limits<int>::max()){
           
            if (right_small == numeric_limits<int>::max()){
            return numeric_limits<int>::max();
        }
            return right_small;
        }
        
        if (right_small == numeric_limits<int>::max()){
            return left_small;
        }*/
        
        if (left_small < right_small){
            counter++;
            return left_small;
        }
        
        else if(right_small <= left_small){
            return right_small;
        }
        
    }
    
    
    int lengthOfLIS(vector<int>& nums) {
        counter = 0;
        
        if (nums.size() == 0){
            return 0;
        }
        
        else if (nums.size() == 1){
            return 1;
        }
        
        else if (nums.size() == 2){
           counter = 1;
        }
        
        else{
            counter = 0;
        }
        
        int size = nums.size()-1;
        int small = smallest_in_left(nums,0,size);
        return counter;
    }
};
