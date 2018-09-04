from math import log, ceil

class Solution(object):
    def smallestGoodBase(self, n):
     
        number = int(n)

        power_ceil = ceil(log(number, 2)) #60
        power_floor = power_ceil - 1

        # if number == ((2**power_ceil ) -1):
        #     return(str(2))

        for base in range(2, number+1):

            while number <= (base ** power_floor):
                power_ceil = power_floor
                power_floor = power_floor - 1

            dig_sum = ((base**power_ceil ) -1) // (base-1)
            print(power_ceil, base, dig_sum) 
            if dig_sum == number:
                return(str(base))


solobj = Solution().smallestGoodBase(14919921443713777)  #2251799813685247 #4681
print(solobj)