#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

unsigned long Factorial(unsigned long n, vector <unsigned long> &mem){

    if(n<=1){
        return 1;
    }

    if(mem[n]!=0){
        return mem[n];
    }

    mem[n] = n*Factorial(n-1,mem);

    return mem[n];

}


void Factorial(unsigned long n){
    vector <unsigned long> mem(n+1,0);
   // memset(mem,0,sizeof(mem));
    cout << Factorial(n,mem);
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    unsigned long n;
    cin >> n;
    Factorial(n);
    return 0;
}
