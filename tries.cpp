#include <iostream>
#include <cassert>

using namespace std;

class node{
    
    public:
    int mark;
    node* children[26];
    
};

node* get()
{
    node* n = new node;
    n -> mark = 0;
    for(int i = 0; i < 26; i++)
    {
        n -> children[i] = NULL;
    }
    return n;
}

void insert_rec(node* temp, string s, int counter){
        
        if(counter == s.length()){
            return;
        }
    
         
        if ( temp->children[s[counter]-'a'] == NULL){
               temp->children[s[counter]-'a'] = new node;
            }
        temp->children[s[counter]-'a']->mark += 1;   
        insert_rec(temp->children[s[counter]-'a'],s,counter+1);
}


void insert(node* temp, string s){
    
        int counter=0;
        insert_rec(temp,s,counter);
    
}



int main()
{
    int n;
    node* root = get();
    cin >> n;
    string type;
    while(n--)
    {
        string s;
        cin >> type >> s;
        assert(s.length() >= 1 && s.length() <= 21);
        node* temp = root;
        if(type == "add")
        {
            insert(temp, s);
        }
        else
        {
            int no = 0;
            for(int i = 0; i < s.length(); i++)
            {
                if(temp -> children[s[i] - 'a'] == NULL)
                {
                    cout << 0 << endl;
                    no = 1;
                    break;
                }
                temp = temp -> children[s[i] - 'a'];
            }
            if(no)
            {
                continue;
            }
            cout << temp -> mark << endl;
        }
    }
}
