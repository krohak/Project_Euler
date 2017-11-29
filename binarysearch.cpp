#include <bits/stdc++.h>
using namespace std;

class IceCream {
    
    public: 
        int flavor; 
        int index;

        IceCream(int flavor, int index) {
            
            this->flavor=flavor;
            this->index=index;
            
       }
};
    
int binarySearch(int first, int last, vector<IceCream> arr, int search) {
    
    while(first<last){
        int middle = (first+last/2)-1;
        
        if(arr[middle].flavor==search){return arr[middle].index;}
        
        else if(arr[middle].flavor<search){first=middle+1;}
        
        else if(arr[middle].flavor>search){last=middle-1;}
        
    }
    
    return -1;
   
}

bool compare(IceCream a, IceCream b){
    
    return a.flavor < b.flavor;
}

int main() {
    int t;
    int n, m;
    cin >> t;
    for(int test = 0; test < t; test++) {       
        cin >> m >> n;
        vector<IceCream> arr;
        arr.reserve(n); 

        for (int i = 0; i < n; i++) {
            int cost;
            cin >> cost;
            arr.push_back(IceCream(cost, i + 1));
        }

        sort(arr.begin(), arr.end(), compare);
        
        int firstIndex = 100000, secondIndex = 100000;
        for(int i = 0; i < n - 1 ; i++) {
            //cout << arr[i].flavor;
            int search = m - arr[i].flavor;
            if(search >= arr[i].flavor) {
                int index = binarySearch( i + 1, n - 1, arr, search);
                if( index != -1 ) {
                    cout << min(arr[i].index, index) << " " << max(arr[i].index, index) << endl;
                    break;

                }
            }
        }

    }

}


