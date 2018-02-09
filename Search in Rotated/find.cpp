class Solution {
public:

  int binary_search (const vector <int> & nums, int & target, int left, int right){

    if (nums.size() == 0){
        return -1;
    }

    while(left<=right){

        int middle = (left+right)/2;

        if (nums[middle] == target){
                return middle;
        }
        else if (nums[middle] < target){
            left = middle+1;
        }
        else if (nums[middle] > target){
            right = middle-1;
        }
    }
    return -1;
  }

  int find_pivot(const vector <int> & nums){

      if (nums.size() <= 1){
        return -1;
      }

      int left = 0;
      int right = nums.size()-1;

      while (left <= right){
        int middle = (left+right)/2;

        if (nums[middle] > nums[middle+1]){
          return middle;
        }
        else if (nums[middle] < nums[middle-1]){
          return middle -1;
        }
        else if (nums[middle] < nums[left]){
          right = middle - 1;
        }
        else if (nums[middle] > nums[right]){
          left = middle + 1;
        }
        else {
            break;
        }

      }

      return -1;

  }



    int search(const vector<int>& nums, int & target) {

        int pivot = find_pivot(nums);
        cout << pivot;

        if (pivot == -1){
          int size = nums.size();
          return binary_search(nums,target,0,size);
        }
        if (target == nums[pivot]){
          return pivot;
        }
        else if (target >= nums[0]){
          return binary_search(nums,target,0,pivot);
        }
        else{
          int size = nums.size();
          return binary_search(nums,target,pivot+1,size);
        }

    }



};
