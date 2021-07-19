from random import randint
from bisect import bisect_left

class Solution:

    def __init__(self, weights):
        self.wList = []
        for i, w in enumerate(weights):
            self.wList.append(
                w+self.wList[i-1] 
                if i > 0 else w
             )

    def pickIndex(self) -> int:
        rand = randint(1, self.wList[-1])
        return bisect_left(self.wList, rand)