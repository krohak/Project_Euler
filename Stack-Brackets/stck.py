# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_matched(expression):
    brackets=[char for char in expression]
    global pairs
    
    if len(brackets)%2 == 1:
        return 0
    
    stck=[]
    while(brackets):
        l=brackets.pop(0)
        if isOpening(l):
            stck.append(l)
         
        else:
            try:
                v=stck.pop()
                if(pairs[v]!=l):
                    return 0
            except:
                return 0
    if stck:
        return 0
    
    return 1
    
      
pairs={'{':'}','(':')','[':']'}

def isOpening(c):
    if(c=='{' or c=='(' or c=='['):
        return 1
    
    return 0

t = int(input().strip())
for a0 in range(t):
    expression = str(input())
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

