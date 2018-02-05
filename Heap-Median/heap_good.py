#!/bin/python3

import sys
import heapq

heap_min=[]
heap_max=[]

def insert_el(a,a_t,heap_min,heap_max):
 
    #print(heap_min,heap_max)
    
    if(not heap_min):
        #print('hel')
        heap_min.append(a_t)
        return
    
    if(not heap_max):
        #print('hi')
        heap_max.append(a_t)
        return
        
    min_high=heap_min[0]
    max_low=heap_max[0]
    
    if(a_t<min_high or (a_t>min_high and a_t<max_low)):
        heap_min.append(a_t)

        
    if(a_t>max_low):
        #print('here')
        heap_max.append(a_t)

               
    #heapq.heapify(heap_max)
    #heapq._heapify_max(heap_min)
    balance(heap_min,heap_max)
        
        
def balance(heap_min,heap_max):
    #print(heap_min,heap_max)
    len_min = len(heap_min)
    len_max = len(heap_max)
    while(abs(len_min-len_max)>1):
        #print('here')
        if (len_min > len_max):
            heap_max.append(heap_min.pop(0))
            len_min -= 1 
            len_max += 1

        else:
            #print(heap_max)
            heap_min.append(heap_max.pop(0))
            len_min += 1 
            len_max -= 1
          
    heapq._heapify_max(heap_min)
    heapq.heapify(heap_max) 
    #print(heap_min,heap_max)
        
def print_median(heap_min,heap_max):
    
    #print((heap_min),(heap_max))
    len_min = len(heap_min)
    len_max = len(heap_max)
    
    if (len_min>len_max):
        #print('hi')
        print(float(heap_min[0]))
        return
              
    if (len_min<len_max):
        #print('hel')
        print(float(heap_max[0]))
        return 
             
              
    print(float(heap_max[0]+heap_min[0])/2)
    return 

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    insert_el(a,a_t,heap_min,heap_max)
    print_median(heap_min,heap_max)
    
