# state is a dict
# { num_stock, profit}

# actions
# buy, sell, cooldown
# actions = set(['b','s','c'])

# conditions
# num_stock > 0 to sell
# need to sell to buy
# one day cooldown after selling

# assumptions
# cooldown can be any day
# cant buy two consecutive days
# cant sell two consecutive days


memo = {}

def generateNextActions(prev_action, state):

    allowed_actions = []
    if prev_action == 'b':
        if state['num_stock'] > 0:
            allowed_actions.append('s')
        allowed_actions.append('c')

    elif prev_action == 's':
        allowed_actions.append('c')

    elif prev_action == 'c':
        allowed_actions.append('b')
        if state['num_stock'] > 0:
            allowed_actions.append('s')
        allowed_actions.append('c')

    return allowed_actions


# apply actions and store in memo table
def applyAction(state, day, prices, action):

    global memo
    # print(day)

    if (day, action) in memo:
        return memo[(day,action)]

    n = len(prices)
    if day < n:


        if action == 'b':
            state['num_stock']+=1
            state['profit']-=prices[day]


        elif action == 's':
            state['num_stock']-=1
            state['profit']+=prices[day]
            

        elif action == 'c':
            pass

       

        # if day < n-1:
        # next action based on updated state and action
        actions = generateNextActions(action, state)
        
        max_profit = 0
        for act in actions:    
            profit = applyAction(state, day+1, prices, act)
            if profit>max_profit:
                max_profit = profit

        memo[(day,action)] = max_profit
        return max_profit

    else:
        return state['profit']
                

        




def main(prices):

    global memo

    # first day we buy
    state={'num_stock':1,'profit':-prices[0]}
    actions = generateNextActions('b', state= state)
    max_p_1 = 0
    for action in actions:
        profit = applyAction(state, 1, prices, action)
        if max_p_1 < profit:
            max_p_1 = profit
    

    # first day we cooldown
    state={'num_stock':0,'profit':0}
    actions = generateNextActions('c', state= state)
    max_p_2 = 0
    for action in actions:
        profit = applyAction(state, 1, prices, action)
        if max_p_2 < profit:
            max_p_2 = profit

    max_profit = max(max_p_1, max_p_2)
    # print(profit1, profit2)

    return max_profit


prices = [1,2,3,0,2]
# prices = [1,2,3,0]

max_profit = main(prices)
print(max_profit)
print(memo)