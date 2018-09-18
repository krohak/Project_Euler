memo = {}

# given previous action and current state,
# generate next actions
def generateNextActions(prev_action, num_stock, bought):

    allowed_actions = []

    if prev_action == 'b':
        if num_stock >= 0:
            allowed_actions.append('s')
        allowed_actions.append('c')

    elif prev_action == 's':
        allowed_actions.append('c')

    elif prev_action == 'c':
        if bought==0:
            allowed_actions.append('b')
        if num_stock > 0:
            allowed_actions.append('s')
        allowed_actions.append('c')

    return allowed_actions


# given action and state, apply action 
# by updating state
def applyAction(action, num_stock, profit, bought, prices, day):

    if action == 'b':
        num_stock+=1
        profit-=prices[day]
        bought=1-bought

    elif action == 's':
        num_stock-=1
        profit+=prices[day]
        bought=1-bought

    elif action == 'c':
        pass

    return num_stock, profit, bought


# iterate the tree and store max profit
# across action branches in memo table
def iterateTree(day, action, num_stock, profit, bought, prices):

    global memo

    # if (day, action) in memo:
    #     return memo[(day,action)]

    if day < len(prices):

        # action and original state
        actions = generateNextActions(action, num_stock, bought)
        # print('Generate Actions: ', day, action, actions, profit)

        # apply the action and update state
        num_stock_updated, profit_updated, bought_updated = applyAction(action, num_stock, profit, bought, prices, day)
        # print('Update State: ',day, action, profit_updated)
        
        max_profit = 0

        # give actions to updated state
        for act in actions:    
            # print("HERE: ",day, act, profit_updated)
            profit_a = iterateTree(day+1, act, num_stock_updated, profit_updated, bought_updated, prices)
            # print("CALCULATED- day:",day+1,", action:", act,", profit:", profit_a)
            # take max across action branches
            if profit_a>max_profit:
                max_profit = profit_a

        memo[(day,action)] = max_profit
        # print("ADDED TO MEMO- day:",day,", action:", action,", max_profit:", max_profit)
        return max_profit

    else:
        # print("END: ",profit)
        return profit


def iterateTreeCaller(prices):
    
    max_profit = 0
    for action in ['b','c']:
        num_stock=0; profit=0; bought=0
        profit_a = iterateTree(0, action, num_stock, profit, bought, prices)
        if profit_a>max_profit:
            max_profit = profit_a

    return max_profit


prices = [1,2,3,0,2]
prices = [1,2,3,0]
prices = [1,2,4,2,5,7,2,4,9,0]

max_profit = iterateTreeCaller(prices)
# print(prices)
print(max_profit)
# print(memo)