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


def Div(x,y):
    if y == 0:
        return 0
    return x//y

def Mul(x,y):
    return x*y

def Add(x,y):
    return x+y

def Sub(x,y):
    return x-y

symbolToFunction = {
    '/':Div,
    '*':Mul,
    '+':Add,
    '-':Sub
}

def evaluateList(expression_list):
    for symbol in symbols:
        new_list = []
        i = 0
        while i< len(expression_list):
            if expression_list[i] == symbol:
                prev = new_list.pop()
                nex = expression_list[i+1]
                result = symbolToFunction[symbol](prev,nex)
                new_list.append(result)
                i+=2
            else:
                new_list.append(expression_list[i])
                i+=1
        expression_list = new_list
    return expression_list[0]


expression = " 3+5 / 2 "
expression = "1+2*5/3+6/4*2"
expression = cleanExpression(expression)
expression_list = expressionToList(expression)
result = evaluateList(expression_list)
print(result)