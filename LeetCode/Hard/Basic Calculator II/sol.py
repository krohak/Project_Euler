symbols = ['/','*','-','+']
symbols_set = set(symbols)

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
    return 0




class Solution(object):
    def calculate(self, expression):
        expression = cleanExpression(expression)
        expression_list = expressionToList(expression)
        result = evaluateList(expression_list)
        return result    