class Solution:
    def compress(self, chars) -> int:
             
        counter = 0
        i = 0
        character_start = 0
        
        while i < len(chars):
            
            character = chars[i]
            
            while i < len(chars) and character == chars[i]:
                chars[i] = None
                counter+=1
                i+=1
            
            chars[character_start] = character
            character_start+=1
            if counter > 1:
                for num_string in "{}".format(counter):
                    chars[character_start] = num_string
                    character_start+=1
            
            counter=0
        
        while not chars[-1]:
            chars.pop()
            
        return len(chars)