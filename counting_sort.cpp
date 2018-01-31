/*

#include <bits/stdc++.h>

int price[n]
int frequency[10004]
int B[10004]

memset(frequency, 0, sizeof(frequency))

for(int i=0; i<n; i++){
  frequency[price[i]]++;
}


for(int i=1; i<10004; i++){
  frequency[i] += frequency[i-1];
}


for(int i=0; i<10004; i++){
  B[frequency[price[i]]] = price[i];
  frequency[i]--;
}

*/

#include<bits/stdc++>
int A[n]
int B[1004]
int C[1004]

memset(C,0,sizeof(C))

for int i; i<n{
  C[A[i]]++
}

for int i; i<1004{
  C[i]+=C[i+1]
}

for int i=n; i>0; i--{
  B[C[A[i]]] = A[i];
  C[A[i]]--;
}
