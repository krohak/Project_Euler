import numpy as np


n=100
random_list = np.random.rand(10)*n

random_int = random_list[7]

random_list.sort()
print(random_list)

def binary_check(num,random_list):

    while (len(random_list) > 0):
        x = len(random_list)//2
        if(random_list[x] == num):
            #print(random_list[x])
            return 1
        elif(random_list[x] > num):
            random_list = random_list[0:x]
        elif(random_list[x] < num):
            random_list = random_list[x:]

    return 0


def binary_search(num,random_list,n):
    first = 1
    last = len(random_list)

    while(first<=last):
        middle = (first+last//2)

        if(random_list[middle] == num):
            return middle
        elif(random_list[middle] > num):
            last = middle-1
        elif(random_list[middle] < num):
            first = middle+1

print(random_int)
#print(binary_check(random_int,random_list))
print(binary_search(random_int,random_list,n))

'''
a = 0
b = n-1
x = a+b/2
'''
