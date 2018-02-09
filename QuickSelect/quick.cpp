class Solution {
public:

    int partition (vector<int>& nums, int l, int r){

      int pivot = nums[l];

      while (l<r){

        while (nums[l] <= pivot){l++;}
        while (nums[r] > pivot){r--;}

        swap(nums[l],nums[r]);

      }

      swap(nums[l],nums[pivot]);

      return l;

    }


    int quick_select(vector<int> & nums, int k, int l, int r){


    if (k > 0 && k <= r - l + 1) {

        int pivot = partition(nums,l,r);
        cout << pivot;

        int target = nums.size() - k;

          if (pivot == target){
            return nums[pivot];
          }

          else if ( pivot < target ){
            return quick_select(nums,k,pivot+1,r);
          }

          else if ( pivot > target ){
            return quick_select(nums,k,l,pivot-1);
          }
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
