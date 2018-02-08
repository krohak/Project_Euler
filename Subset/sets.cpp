class Solution {
public:
    vector<vector<int>> result;


    void subset(vector<int> result_set,vector<int> super_set, int i){

        if (i >= super_set.size()){
            result.push_back(result_set);
            return;
        }

        subset(result_set,super_set,i+1);

        result_set.push_back(super_set[i]);

        subset(result_set,super_set,i+1);

        return;

    }


    vector<vector<int>> subsets(vector<int>& nums) {

        int i = 0;
        vector<int> result_set;

        subset(result_set,nums,i);

        return result;
    }
};
