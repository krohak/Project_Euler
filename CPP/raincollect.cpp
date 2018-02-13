#include <stdio.h>
#include <iostream>

using namespace std;

int findWater(int arr[],int n){
    
    /*
    1. keep counter left=0, and couter right=n-1
    2. keep left max and right max = 0, result = 0
    3. while counter left<= right
    4. if arr[left] < arr[right], 
        - if left_max < arr[left], arr[left] = left_max
        - else, result += left_max - arr[left]
        - increment left
    5. do same for right
    */
    
    int left = 0;
    int right = n-1;
    int left_max,right_max,result=0;
    
    while (left<=right){
        
        if (arr[left] < arr[right]){
            
            if (left_max < arr[left])
                left_max = arr[left];
                
            else{
                result+= (left_max - arr[left]);
                left++;
            }
                
            
        }
        
        else{
            
            if (right_max < arr[right])
                right_max = arr[right];
            
            else{
                result+= (right_max - arr[right]);
                right--;
            }
            
        }
        
        
    }
    
    return result;
    
    
}


int main()
{
    int arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "Maximum water that can be accumulated is "
        << findWater(arr, n); 
}
