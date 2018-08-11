symbols_set = set(['/','*','+','-',' '])

def isSymbol(char):
    global symbols_set
    if char in symbols_set:
        return 1
    else:
        return 0


def cleanExpression(expression):
    return expression.replace(" ","")


def expressionToList(expression):
    expression_list = []

    exp_size = len(expression)
    i = 0
    while i<exp_size:
        num_str = ""
        while i<exp_size:
            if not isSymbol(expression[i]):
                num_str+=expression[i]
                i+=1
            else:
                break
        num = int(num_str)
        if i<exp_size:
            symbol = expression[i]
        else:
            symbol = " "
        expression_list.append(num)
        expression_list.append(symbol)
        i+=1

    return expression_list


def evaluateList(expression_list):
    md = -1
    sign = 1
    result = 0
    prev = 0

    i = 0
    while i<len(expression_list):
        if not isSymbol(expression_list[i]):
            if md == 0:
                prev *= expression_list[i]
                md = -1
            elif md ==  1: 
                prev //= expression_list[i]
                md = -1
            else:
                prev = expression_list[i]
        
        else:
            if expression_list[i] == '/':
                md = 1
            elif expression_list[i] == '*':
                md = 0
            elif expression_list[i] == '+':
                result += sign*prev
                sign = 1
            elif expression_list[i] == '-':
                result += sign*prev
                sign = -1   
        i+=1
    result += sign*prev
    return result


class Solution(object):
    def calculate(self, expression):
        expression = cleanExpression(expression)
        expression_list = expressionToList(expression)
        result = evaluateList(expression_list)
        return result    


expression = "3+2*2"
result = Solution().calculate(expression)
print(result)