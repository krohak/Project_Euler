class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        back_products = goBack(nums)
        fow_products = goForward(nums)

        back_products.pop()
        fow_products.pop()

        size = len(back_products)

        answer = []
        for i in range(size):
            answer.append(fow_products[i]*back_products[size-1-i])

        return answer
        

'''
traverse array backward
    compute multiplication of right part at each step using mult of prev right
    store in memo
'''
def goBack(arr):

    back_products = []
    back_products.append(1)

    i = 0
    for elem in reversed(arr):
        back_products.append(back_products[i]*elem)
        i+=1
    return back_products


'''
traverse forward
    compute multiplication of left part using mult of prev left
    lookup right from memo
'''
def goForward(arr):

    fow_products = []
    fow_products.append(1)

    i = 0
    for elem in arr:
        fow_products.append(fow_products[i]*elem)
        i+=1
    return fow_products
