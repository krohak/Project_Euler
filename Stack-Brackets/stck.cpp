#include <stack>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;

    

bool is_balanced(string expression, char opening[], char closing[]) {
    
    stack <char> open_stack;
    
    
    for(int i=0; i<expression.length(); i++){
        
	// to check if we have pushed the current char
        bool pushed = 0;
        
	// check if char is open bracket and push it
        for(int j=0; j<3; j++){
            if(expression[i] == opening[j]){
                open_stack.push(opening[j]);
                pushed = 1;
            }
        }
        
	// if closed bracket, compare against the open_stack top
         if (!pushed){
             
	     // store popped char
             char popped;

	     // check if stack not empty
             if(open_stack.size() > 0){
             popped = open_stack.top();
             open_stack.pop();
             }

	     // if stack empty, expression not valid
             else{
                 return 0;
             }
             

	     // if popped open bracket does not match with closing bracket, expression not valid
             for(int j=0; j<3; j++){
                 
                 if(popped == opening[j] &&  expression[i] != closing[j] ){
                    
                     return 0;
                 }
                 
             }
             
         }
            
        
       
        
    }
    
    // if stack not empty in the end, expression not valid
    if(!open_stack.empty()){
        return 0;
    }

    // valid expression
    return 1;
    
    
    
    
    
}

int main(){
    int t;
    
    char opening[3];
    opening[0]='('; 
    opening[1]= '['; 
    opening[2]= '{';
    
    char closing[3];
    closing[0]=')'; 
    closing[1]= ']'; 
    closing[2]= '}';
    
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        string expression;
        cin >> expression;
        bool answer = is_balanced(expression, opening, closing);
        if(answer)
            cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}

