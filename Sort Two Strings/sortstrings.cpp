#include <iostream>
#include <string>
#include <unordered_map>
#include <map>

using namespace std;


string sort_strings(string first, string second){
        map<char,int> hash_table;
        map<char,int>::iterator itr_map;

        for (int i=0; i<first.length(); i++) {
                if (!hash_table.count(first[i])) {
                        hash_table[first[i]] = 0;
                }
                else{
                        hash_table[first[i]] += 1;
                }
        }

        for (int i=0; i<second.length(); i++) {
                if (!hash_table.count(second[i])) {
                        hash_table[second[i]] = 0;
                }
                else{
                        hash_table[second[i]] += 1;
                }
        }

        string third = "";


        /*
           // For unordered_map

           for(char j = 'a'; j<= 'z'; j++ ){
            if(hash_table.count(j)){
              for(int i = 0; i<=hash_table[j]; i++){
                third+=j;
                //cout << j;
              }
            }
           }*/


        // For ordered map

        // Vanilla
        /*  for (itr_map = hash_table.begin(); itr_map != hash_table.end(); itr_map++){
            for (int i = 0; i<=(*itr_map).second; i++){
              third+=(*itr_map).first;
            }
           }*/

        // Range
        for (auto elem: hash_table) {
                for (int i=0; i<= elem.second; i++) {
                        third+= elem.first;
                }
        }

        return third;

}



int main(){

        string result = sort_strings("wdcefvrgbtg","ujllllllhbtgvrfd");
        cout << result << endl;

        return 0;
}
