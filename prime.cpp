#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


void isPrime(const int &n){

      if (n==1){
          cout << "Not prime" <<endl;
          return;
      }

      for (int i=2; i<=sqrt(n); i++){
          if (n%i == 0){
              cout << "Not prime" << endl;
              return;
          }
      }

    cout << "Prime" << endl;
    return;
}

int main(){
    int p;
    cin >> p;
    for(int a0 = 0; a0 < p; a0++){
        int n;
        cin >> n;
        isPrime(n);
        }
    return 0;
}
