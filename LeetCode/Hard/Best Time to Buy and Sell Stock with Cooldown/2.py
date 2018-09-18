memo = {}

# given previous action and current state,
# generate next actions
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


# given action and state, apply action 
# by updating state
def applyAction(action, state, prices, day):

    if action == 'b':
        state['num_stock']+=1
        state['profit']-=prices[day]


    elif action == 's':
        state['num_stock']-=1
        state['profit']+=prices[day]
        

    elif action == 'c':
        pass

    return state


# iterate the tree and store max profit
# across action branches in memo table
def iterateTree(day, action, state, prices):

    global memo

    if (day, action) in memo:
        return memo[(day,action)]

    if day < len(prices):

        # action and original state
        actions = generateNextActions(action, state)

        # apply the action and update state
        state = applyAction(action, state, prices, day)
       
        
        max_profit = 0

        # give actions to updated state
        for act in actions:    
            profit = iterateTree(day+1, act, state, prices)
            # take max across action branches
            if profit>max_profit:
                max_profit = profit

        memo[(day,action)] = max_profit
        return max_profit

    else:
        return state['profit']


def iterateTreeCaller(prices):
    
    max_profit = 0
    for action in ['b','c']:
        state={'num_stock':0,'profit':0}
        profit = iterateTree(0, action, state, prices)
        if profit>max_profit:
            max_profit = profit

    return max_profit


prices = [1,2,3,0,2]
max_profit = iterateTreeCaller(prices)
print(max_profit)
print(memo)