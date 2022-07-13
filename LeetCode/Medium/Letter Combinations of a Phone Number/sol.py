class Solution(object):
    def __init__(self):
        self.mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        }
        self.combinations = []
        self.digits = ''

    def letterCombinations(self, digits):
        self.digits = digits
        self.recursiveCombinations(0, '')
        return self.combinations

    def recursiveCombinations(self, i, combination):
        if i >= len(self.digits): 
            self.combinations.append(combination)
            return
        for c in self.mapping[self.digits[i]]:
            self.recursiveCombinations(i+1, combination+c)
        return


print(Solution().letterCombinations("2"))