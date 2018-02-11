/*
- #include<algorithm> 
- #include<vector>
- vector<float> heap;
- make_heap(heap.begin(),heap.end(),compare())
- heap.push_back(number)
- push_heap(heap.begin(),heap.end(),compare())
- pop_heap(heap.begin(),heap.end(),compare())
- heap.pop_back(number)
- heap.front()
*/

#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;


void print_heap(vector<float> & min_heap, string n){
    
    cout << "heap " << n << ": " ;
    
    for(int i=0; i<min_heap.size(); i++){
        cout << min_heap[i] << " ";    
    }
    
    cout << endl;
}


// min heap
struct compare{
bool operator()(const float &a, const float &b){
    return a>b;
}
};

void heapify(vector<float> & min_heap,vector<float> & max_heap,float number){
    
    // create initial heaps
    if(min_heap.size() == 0){
        min_heap.push_back(number);
        push_heap(min_heap.begin(), min_heap.end());
    }
    
    else if(max_heap.size() == 0){
        if(number > min_heap.front()){
            max_heap.push_back(number);
            push_heap(max_heap.begin(),max_heap.end(),compare());
        }
        
        else{
            min_heap.push_back(number);
            push_heap(min_heap.begin(),min_heap.end());
        }
    }
    
    //add the number to existing heaps
    
    else if(max_heap.front() >= number){
        min_heap.push_back(number);
        push_heap(min_heap.begin(), min_heap.end());
    }
    
    else {
        max_heap.push_back(number);
        push_heap(max_heap.begin(), max_heap.end(), compare());
    }
    
    //cout << "before balance" <<endl;
    //print_heap(min_heap, "min" );
    //print_heap(max_heap, "max" );
    
    //maintain the balance
    int min_heap_size = min_heap.size();
    int max_heap_size = max_heap.size();
        
    if(max_heap_size-min_heap_size >= 2){
        
        min_heap.push_back(max_heap.front());
        push_heap(min_heap.begin(), min_heap.end());
        
        pop_heap (max_heap.begin(),max_heap.end(),compare()); max_heap.pop_back();
    }
    
    else if(min_heap_size-max_heap_size >= 2){
       
        max_heap.push_back(min_heap.front());
        push_heap(max_heap.begin(), max_heap.end(),compare());
        
        pop_heap (min_heap.begin(),min_heap.end()); min_heap.pop_back();
    }

    //cout << "after balance" <<endl;
    //print_heap(min_heap, "min" );
    //print_heap(max_heap, "max" );
   
}


void print_median(vector<float> & min_heap, vector<float> & max_heap,float number){
    

    heapify(min_heap,max_heap,number);

    if(max_heap.size() == 0){
        cout << fixed << setprecision(1) << (min_heap.front()) << endl;
    }
    
    else if(min_heap.size()>max_heap.size()){
        cout << fixed <<setprecision(1) << (min_heap.front()) << endl;
    }
    
    else if(min_heap.size()<max_heap.size()){
        cout << fixed <<setprecision(1) << (max_heap.front()) << endl;
    }
    
    else{
        
        cout <<fixed << setprecision(1) << (min_heap.front()+max_heap.front())/2 <<endl;
    }
}


int main(){
    int n;
    vector<float> min_heap;
    vector<float> max_heap;
    make_heap(min_heap.begin(), min_heap.end());
    make_heap(max_heap.begin(), max_heap.end(), compare());
    
    cin >> n;
    float number;
    for(int a_i = 0;a_i < n;a_i++){
       cin >> number;
       print_median(min_heap,max_heap,number);
      // cout << endl;
    }
    return 0;
}

