from math import log, ceil

class Solution(object):
    def smallestGoodBase(self, n):
     
        number = int(n)

        power_ceil = 60 #ceil(log(number, 2)) 
        power_floor = power_ceil - 1

        # if number == ((2**power_ceil ) -1):
        #     return(str(2))
        base = 2
        while base <= number:

            while number <= (base ** power_floor):
                power_ceil = power_floor
                power_floor = power_floor - 1

            dig_sum = ((base**power_ceil ) -1) // (base-1)
            print(power_ceil, base, dig_sum) 
            if dig_sum == number:
                return(str(base))

            base+=1



solobj = Solution().smallestGoodBase(470988884881403701)  #14919921443713777 #2251799813685247 #4681
print(solobj)