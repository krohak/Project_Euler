#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;


string sort_strings(string first, string second){
    unordered_map<char,int> hash_table;
    unordered_map<char,int>::iterator itr_map;

    for (int i=0; i<first.length(); i++){
      if (!hash_table.count(first[i])){
        hash_table[first[i]] = 0;
      }
      else{
        hash_table[first[i]] += 1;
      }
    }

    for (int i=0; i<second.length(); i++){
      if (!hash_table.count(second[i])){
        hash_table[second[i]] = 0;
      }
      else{
        hash_table[second[i]] += 1;
      }
    }

    string third = "";


    for(char j = 'a'; j<= 'z'; j++ ){
      if(hash_table.count(j)){
        for(int i = 0; i<=hash_table[j]; i++){
          third+=j;
          //cout << j;
        }
      }
    }

    return third;

}



int main(){

  string result = sort_strings("wdcefvrgbtg","ujyeeeeeeeeeeehbtgvrfd");
  cout << result << endl;

  return 0;
}
