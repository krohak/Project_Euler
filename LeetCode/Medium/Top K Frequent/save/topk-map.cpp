typedef pair<int, int> int_pair;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<int> result;
        priority_queue <int_pair ,vector <int_pair>> pq;
       
        
        unordered_map <int,int> map;
        
        for (auto i: nums){
            map[i]++;
        }
        
        for (auto itr: map){
            pq.push(make_pair(itr.second,itr.first));
        }
        
        
        
        while (k>0){
            int i = pq.top().second;   pq.pop();
            result.push_back(i);
            k--;
        }
        
        return result;
        
    }
};
