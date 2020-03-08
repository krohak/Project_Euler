class Fraction:
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def __add__(self, frac):
        
        den_set = set([self.den, frac.den])
        lcm = 1
        for den in den_set:
            lcm *= den
        
        first_num = self.num * (lcm//self.den)
        second_num = frac.num * (lcm//frac.den)
        
        hcf = self.hcf((first_num+second_num), lcm)
        
        return Fraction((first_num+second_num)//hcf, (lcm)//hcf)
    
    def __repr__(self):
        return "{}/{}".format(self.num, self.den)
    
    def hcf(self, a, b):
        
        a,b = abs(a), abs(b)
        while(b):
            a, b = b, a%b
        
        return a

class Solution:
    def fractionAddition(self, expression):
        
        fractions = self.parse_fraction_list(expression)
        
        frac_sum = Fraction(0,1)
        for fraction in fractions:
            frac_sum += fraction
        
        if frac_sum.num == 0:
            return "0/1"
        
        return str(frac_sum)
              
    
    
    def parse_fraction_list(self, expression):
    
        n = len(expression)    
        fractions = []
        negative = False
        
        i = 0
        while i < n:
            
            num = ""
            den = ""
            found_slash = False
            while i<n and not self.is_plus_minus(expression[i]):
                
                char = expression[i]
                
                if char == '/':
                    found_slash = True
                
                elif not found_slash:
                    num += char
                else:
                    den += char
                
                i+=1
            
            if found_slash:
                num = -1*int(num) if negative else int(num)
                den = int(den)
                fractions.append(Fraction(num,den))
            
            if i<n and expression[i]=='-':
                negative = True
            else:
                negative = False
                
            i+=1
        
        return fractions
    
    def is_plus_minus(self, char):
        return True if (char=='-' or char=='+') else False