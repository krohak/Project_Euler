'''
Prototype code in case given a
n-sq matrix instead of n*m one
'''

n = 2
n_sq = n**2

elements = range(1,n_sq+1)

row_step = n
col_step = n

pointer = 0
count = 1

# print first element
print(elements[0])

while count<n_sq:
    
    # forward
    i = 0
    while i<col_step-1:
        i+=1
        pointer+=1
        print(elements[pointer])
        count+=1
        
    if count>=n_sq:
        break
    
    # down
    i = 0
    while i<row_step-1:
        i+=1
        pointer+=row_step
        print(elements[pointer])
        count+=1

    if count>=n_sq:
        break

    # back
    i = 0
    while i<col_step-1:
        i+=1
        pointer-=1
        print(elements[pointer])
        count+=1

    if count>=n_sq:
        break

    # up    
    i = 0
    while i<row_step-1:
        i+=1
        pointer-=row_step
        print(elements[pointer])
        count+=1

    if count>=n_sq:
        break