class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if not numerator:
            return "0"
        
        remainder_dict = {}
        
        decimal_string = ""
        
        if (numerator < 0) ^ (denominator < 0):
            decimal_string = "-"
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        quotient = numerator//denominator
        remainder = numerator%denominator
        
        decimal_string = "{}{}".format(decimal_string, quotient)
        
        if remainder:
            decimal_string = "{}.".format(decimal_string)
        
        i = 0
        while remainder:
            numerator = remainder*10
            quotient = numerator//denominator
            
            if remainder in remainder_dict:
                break
            
            else:
                remainder_dict[remainder] = i
                i+=1   
                decimal_string = "{}{}".format(decimal_string, quotient)
                remainder = numerator%denominator
        
        if remainder:
            before_decimal, after_decimal = decimal_string.split('.')
            open_at = remainder_dict[remainder]
            after_decimal = "{}{}{}{}".format(after_decimal[:open_at], '(', after_decimal[open_at:], ')')
            decimal_string = "{}.{}".format(before_decimal, after_decimal)
        
        return decimal_string
            
            