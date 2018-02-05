#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef struct node
{
    int mark;
    node* children[26];
} node;

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

void insert(node* root, string s)
{
    for(int i = 0; i < s.length(); i++)
    {
        int now = s[i] - 'a';
        if(root -> children[now] == NULL)
        {
            root -> children[now] = get();
        }
        root = root -> children[now];
        root -> mark += 1;
    }
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
