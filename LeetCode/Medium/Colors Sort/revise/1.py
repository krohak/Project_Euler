def sortColors(nums):
    
    n = len(nums)
    red = 0
    white = 0
    blue = n-1


    while (red<blue and white<n):
        while(white<n and nums[white] != 1):
            white+=1

        while(white<n and nums[white] == 1):
            white+=1

        while(nums[red] == 0 and red<n):
            red+=1
        
        while(nums[blue] == 2 and blue>=0):
            blue-=1
        
        if(nums[red] == 2 and nums[blue] == 0):
            nums[red], nums[blue] = nums[blue], nums[red]
            red+=1
            blue-=1
        
        elif(nums[red] == 2 and nums[blue] == 1):
            nums[blue], nums[red] = nums[red], nums[blue]
            blue-=1

        elif(nums[red] == 1 and nums[blue] == 0):
            nums[blue], nums[red] = nums[red], nums[blue]
            red+=1

        elif(nums[red] == 1 and nums[blue] == 1):
            red+=1
            blue-=1

    print(red, white, blue)
    return nums


nums = [2,0,2,1,1,0]

nums = [1,1,1,0,2,0,2,0,2]
sorted_nums = sortColors(nums)
print(sorted_nums)