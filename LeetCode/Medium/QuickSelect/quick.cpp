class Solution {
public:

    int partition (vector<int>& nums, int l, int r){

    int x = nums[r], i = l;
    for (int j = l; j < r ; j++) {
        if (nums[j] <= x) {
            swap(nums[i], nums[j]);
            i++;
        }
    }
    swap(nums[i], nums[r]);
    return i;

    }


    int quick_select(vector<int> & nums, int k, int l, int r){


        int pivot = partition(nums,l,r);
        cout << pivot <<endl;

        int target = nums.size() - k;

          if (pivot == target){
            cout << "anser";
            return nums[pivot];
          }

          else if ( pivot < target ){
            return quick_select(nums,k,pivot+1,r);
          }

          else if ( pivot > target ){
            return quick_select(nums,k,l,pivot-1);
          }
    }


       int findKthLargest(vector<int>& nums, int k) {
           if (nums.size() == 1){
               return nums[0];
           }


           int size = nums.size()-1;
           return quick_select(nums,k,0,size);
    }

};
