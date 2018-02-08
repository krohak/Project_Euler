class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int i =0;
        int blu = nums.size() -1; int red = 0;
        
        
        while (i <= blu){
            
            if ( nums[i] == 0 ){
                swap(nums[i],nums[red]);
                i++;
                red++;
                continue;
            }
            
            else if (nums[i] == 2){
                swap(nums[i],nums[blu]);
                blu--;
                continue;
            }
            
            i++;
        }
    }
};
