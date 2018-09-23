class Solution {
    public:
        int maxProfit(int k, vector<int>& prices) {
            
            int m = prices.size();
            if(m==0 || m==1 || k == 0) return 0;
            if (k>m/2){ // simple case
                int ans = 0;
                for (int i=1; i<m; ++i){
                    ans += max(prices[i] - prices[i-1],0);
                }
                return ans;
            }


            vector<vector<int>> buy(k+1,vector<int>(m+1,0));
            vector<vector<int>> sell(k+1,vector<int>(m+1,0));


            
            for(int i=1;i<=k;i++)
                buy[i][0] = INT_MIN;

            
                
            for(int i=1;i<=m;i++){
                for(int j=1;j<=k;j++){
                    //for the first buy state, need to compare the current price with the previous price. sell[0][0] are all initialized with 0, then sell[0][0] - prices[i-1] is the price of current first buy state
                    buy[j][i] = max(buy[j][i-1], sell[j-1][i-1] - prices[i-1]);
                    sell[j][i] = max(buy[j][i-1]+prices[i-1],sell[j][i-1]);
                }
            }
            

            for(int i=1;i<=m;i++){
                for(int j=1;j<=k;j++){
                    
                    cout << i << " " << j << " " << sell[j][i] <<endl;
                }
            }

            for(int i=1;i<=m;i++){
                for(int j=1;j<=k;j++){
                    
                    cout << i << " " << j << " " << buy[j][i] <<endl;
                }
            }
            
            return sell[k][m];
        }
    };