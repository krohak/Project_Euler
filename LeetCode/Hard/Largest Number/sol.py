
class MyInt(int):

    def __lt__(a, b):
        x = int(str(a)+str(b))
        y = int(str(b)+str(a))

        return x<y
    
    def __gt__(a, b):
        return not self.__lt__(a,b)



class Solution:
    def largestNumber(self, arr):

        if len(arr) == 0 or sum(arr)==0:
            return "0"
        elif len(arr) == 1:
            return str(arr[0])
        
        nums = []
        for element in arr:
            nums.append(MyInt(element))

        ret_str = ""
        for element in reversed(sorted(nums)):
            ret_str+=str(element)

        return ret_str



arr = [3,30,34,5,9]
longest = Solution().largestNumber(arr)
print(longest)