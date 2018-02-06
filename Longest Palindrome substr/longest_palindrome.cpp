class Solution {
public:
 
       int expand(string s, int i, int j){
        
        int L = i;
        int R = j;
        
        while(L>=0 && R < s.length() && s[R] == s[L]){
            L--;
            R++;
        }
        
        return R - L - 1;
    }
    
    string longestPalindrome(string s) {
        int start = 0; 
        int end = 0;
        
        for (int i=0; i<s.length(); i++){
            int len1 = expand(s,i,i);
            int len2 = expand(s,i,i+1);
            
            int len = max(len1,len2);
            
            if (len > end ) {
            start = i - (len - 1) / 2;
            end = len ;
            }
        }
        
        return s.substr(start, end );
    }
    
 
};
