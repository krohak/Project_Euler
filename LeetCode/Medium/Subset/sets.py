from copy import deepcopy

result=[]

def subset(result_set,super_set,i):

    if i >= len(super_set):
        print(result_set)
        global result
        result.append(result_set)
        return

    result_set1 = deepcopy(result_set)
    result_set2 = deepcopy(result_set)

    subset(result_set1,super_set,i+1)
    result_set2.append(super_set[i])
    subset(result_set2,super_set,i+1)
    return


a=[]
b=[0]
subset(a,b,0)
print(result)
