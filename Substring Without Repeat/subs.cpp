#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_map <char,int> hashmap;

        int i = 0;
        int j = 0;

        int result = 0;
        int final_result = 0;

        while( j<s.length()){

            if(!hashmap.count(s[j])){
                hashmap[s[j]] = j;
                j++;
                result++;
            }

            else{
                if (hashmap[s[j]] == i){
                    hashmap[s[j]] = j;
                    j++;
                    i++;
                }

                else{

                    if(result>final_result){final_result=result;}
                    i = j = hashmap[s[j]]+1;
                    hashmap.clear();
                    result = 0;
                }
            }

        }

        if(result>final_result){final_result=result;}
        return final_result;
    }
};
