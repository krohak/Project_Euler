typedef pair<int, int> int_pair;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<int> result;
        priority_queue <int_pair ,vector <int_pair>> pq;
        vector<int>::iterator itr;
        vector<int>::iterator lower;
        vector<int>::iterator upper;
        
        sort(nums.begin(),nums.end());

        itr = nums.begin();
        
        while(itr<nums.end()){
            
            lower = lower_bound(nums.begin(),nums.end(),*itr);
            upper = upper_bound(nums.begin(),nums.end(),*itr);
            
            int freq = upper - lower;
            
            pq.push(make_pair(freq,*itr));
            
            itr = upper;
        }
        
        while (k>0){
            int i = pq.top().second;   pq.pop();
            result.push_back(i);
            k--;
        }
        
        return result;
        
    }
};
