class Solution(object):
    def isNumber(self, s):
        if (s.find('e') !=- 1) ^ (s.find('E') !=- 1):
            epos = max(s.find('e'), s.find('E'))
            if epos==0 or epos == len(s)-1: return False
            firstHalf, secondHalf = s[:epos], s[epos+1:]
            if (self.isDecimal(firstHalf) or self.isInteger(firstHalf)) and self.isInteger(secondHalf): return True
            return False
        elif self.isDecimal(s) or self.isInteger(s): return True
        return False
        
    def isDecimal(self, ns):
        if self.isSign(ns[0]): ns = ns[1:]
        if ns.find('.') == -1 or len(ns.split('.'))>2: return False
        ns = ''.join(ns.split('.'))
        return all([ self.isDigit(n) for n in ns ]) if ns else False


    def isInteger(self, ns):
        if self.isSign(ns[0]): ns = ns[1:]
        return all([ self.isDigit(n) for n in ns ]) if ns else False


    def isDigit(self, ns):
        if ord(ns) >= 48 and ord(ns) <= 57: return True
        return False
        
    def isSign(self, ns):
        if ns=='+' or ns=='-': return True
        return False



# s = ["2", "0089", "-0.1", "+3.14", "4.", "-.9" ]
#[ "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# s = "-123.456e789"
# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
s = "+1."
print(Solution().isNumber(s))