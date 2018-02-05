#include <bits/stdc++.h>
#include <unordered_map>
#include <string> 

using namespace std;

long getWays(long n, vector <long> c, int index, unordered_map <string,long> memo ){
    
    if(n == 0){
        return 1;
    }
    
    if(index >= c.size()){
        return 0;
    }
    
    string key;
    key = to_string(n) + '-' + to_string(index);
    
    if(memo.count(key)){
        return memo[key];
    }
    
    long ways = 0;
    long new_n = n;
    
    while(new_n >= 0){
        ways+=getWays(new_n,c,index+1,memo);
        new_n-=c[index];
    }
    
    
    memo[key] = ways;
    
    return ways;
}

long getWays(long n, vector < long > c){
    // Complete this function
    unordered_map <string,long> memo;
    return getWays(n,c,0,memo);
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<long> c(m);
    for(int c_i = 0; c_i < m; c_i++){
       cin >> c[c_i];
    }
    // Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    long ways = getWays(n, c);
    cout << ways;
    return 0;
}

