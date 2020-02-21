class Solution:

    def __init__(self):
        self.text_arr = []
        self.n = 0
        self.stable = False

    def candy_crush_caller(self, text):
        self.text_arr = list(text)

        self.n = len(self.text_arr)

        while not self.stable:
            self.candy_crush()
        
        text = self.clean_text_arr()

        return text

    def candy_crush(self):
        i = 0
        self.stable = True
        while i < self.n:
            if self.text_arr[i]:
                i = self.find_consecutive(i)
            else:
                i+=1
    
    def find_consecutive(self, i):
        
        pointer = i
        char = self.text_arr[i]
        counter = 0

        while(pointer<self.n):
            if self.text_arr[pointer] == char:
                counter+=1
            elif not self.text_arr[pointer] == None:
                break
            pointer+=1
        
        if(counter>=3):
            self.stable = False
            for p in range(i, pointer):
                if self.text_arr[p]:
                    self.text_arr[p] = None
        
        return pointer

    def clean_text_arr(self):

        text_arr = []
        for i in range(0, self.n):
            if not self.text_arr[i] == None:
                text_arr.append(self.text_arr[i])

        text = ''.join(text_arr)
        return text


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