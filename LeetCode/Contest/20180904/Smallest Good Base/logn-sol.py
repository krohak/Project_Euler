import math

class Solution(object):
    def smallestGoodBase(self, num):
        
        num = int(num)
        length = int(math.log(num,2))+1
        # +1 for lowest number in the format '1000..'
        # greater than num

        while length>2:

            base = int(num**(1.0/(length-1)))
            # length-1 corresponds to the num

            if num == ((base**length)-1) // (base-1): 
                # '//' for int conversion
                return str(base)
            
            length-=1

        return str(num-1)


ans = Solution().smallestGoodBase("14919921443713777")
print(ans)
