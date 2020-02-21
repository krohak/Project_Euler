

class Solution:

    def __init__(self):
        self.text_arr = []
        self.n = 0
        self.stable = False

    def candy_crush_caller(self, text):
        while not self.stable:
            text = self.candy_crush(text)
        return text

    def candy_crush(self, text):

        self.text_arr = list(text)

        self.n = len(self.text_arr)

        i = 0
        while i < self.n:
            i = self.find_consecutive(i)

        text = self.clean_text_arr()

        return text

    
    def clean_text_arr(self):

        text_arr = []
        self.stable = True
        for i in range(0, self.n):
            if not self.text_arr[i] == None:
                text_arr.append(self.text_arr[i])
            else:
                self.stable = False

        text = ''.join(text_arr)

        return text
    
    def find_consecutive(self, i):
        
        pointer = i
        char = self.text_arr[i]
        counter = 0

        while(pointer<self.n and self.text_arr[pointer] == char):
            counter+=1
            pointer+=1

        pointer = i
        if(counter>=3):
            while(counter):
                self.text_arr[pointer] = None
                pointer+=1
                counter-=1
        
            return pointer
        else:
            return pointer+1


test = "aaabbbc"
# Output: "c"
test = "aabbbacd"
# Output: "cd"
test = "aabbccddeeedcba"
# Output: ""
test = "aaabbbacd"
# Output: "acd"

sol = Solution().candy_crush_caller(test)
print(sol)