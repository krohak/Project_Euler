def sortColors(nums):
    
    n = len(nums)
    red = 0
    white = 0
    blue = n-1

    while(white<=blue):

        if(nums[white] == 0):
            nums[red], nums[white] = nums[white], nums[red]
            red+=1
            white+=1        
        elif(nums[white] == 2):
            nums[blue], nums[white] = nums[white], nums[blue]
            blue-=1
        else: white+=1
    return nums

nums = [2,0,2,1,1,0]

nums = [1,1,1,0,2,0,2,0,2]
sorted_nums = sortColors(nums)
print(sorted_nums)