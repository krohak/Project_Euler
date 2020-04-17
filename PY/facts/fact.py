
def func(array): 
     for num in array: 
        if num%2==0: 
            print(num) 
            break # Case1: Break is called, so 'else' wouldn't be executed. 
     else: # Case 2: 'else' executed since break is not called 
        print("No call for Break. Else is executed")  
  
print("1st Case:") 
a = [2] 
func(a) 
print("2nd Case:") 
a = [1] 
func(a) 
