#!/bin/python3

import sys
import heapq

heap_min=[]
heap_max=[]

def insert_el(a,a_t):
    for i,el in enumerate(a):
        #print(el)
        if a_t < el:
            a.insert(i,a_t)
            return 
    
    a.append(a_t) 

def print_median(a):
    leng=len(a)
    first,second,median = 0,0,0
    
    if leng==1:
        print(float(a[0]))
        return
    
    elif leng%2 == 1:
        first=(leng//2)
        median=a[first]
        print(float(median))
        return 
    
    else:
        first=(leng//2)-1
        second=first+1
        median=(a[first]+a[second])/2
        print(float(median))
        return 
    

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    insert_el(a,a_t)
    #print(a)
    print_median(a)
    
