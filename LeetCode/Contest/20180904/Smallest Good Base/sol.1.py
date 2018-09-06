from math import log, ceil, floor

class Solution(object):
    def smallestGoodBase(self, n):
     
        number = int(n)

        power_ceil = ceil(log(number, 2)) 

        base = 2
        while base <= number:

            dig_sum = ((base**power_ceil ) -1) // (base-1)
            diff = dig_sum - number
            print(power_ceil, base, dig_sum) 
            if dig_sum == number:
                return(str(base))
            # if dig_sum <= 686286299: 
                # print('oh')
                # return('0')
 
            base+=1
            # power_ceil = ceil(power_ceil / log(base,base-1))
            # power_ceil = ceil(log(number, base)) 
            # return power_ceil

solobj = Solution().smallestGoodBase(470988884881403701) #470988884881403701  #2251799813685247 #4681 #14919921443713777
print(solobj)