class Solution:
    def __init__(self):
        self.possibilities = []
        self.mapping = {
            '2' :['a', 'b', 'c'],
            '3' :['d', 'e', 'f'],
            '4' :['g', 'h', 'i'],
            '5' :['j', 'k', 'l'],
            '6' :['m', 'n', 'o'],
            '7' :['p', 'q', 'r','s'],
            '8' :['t', 'u', 'v'],
            '9' :['w', 'x', 'y', 'z']
        }
        self.digits = ""
    
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        self.digits = digits
        self.recurseCombinations("", 0)
        return self.possibilities
        
    
    def recurseCombinations(self, combString, pointer):
        if pointer >= len(self.digits):
            self.possibilities.append(combString)
            return 
        
        letters = self.mapping[self.digits[pointer]]
        for l in letters:
            self.recurseCombinations(combString+l, pointer+1)