

# state is a dict
# {day, num_stock, profit}

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

    n = len(prices)
    if day < n:


        if action == 'b':
            state['num_stock']+=1
            state['profit']-=prices[day]

            actions = generateNextActions( 'b', state= state)


        elif action == 's':
            state['num_stock']-=1
            state['profit']+=prices[day]

            actions = generateNextActions( 's', state= state)

        elif action == 'c':
            actions = generateNextActions( 'c', state= state)

        for action in actions:
            profit = applyAction(state, day+1, prices, action)

    else:
        return state['profit']




def main(prices):

    num_stock = 0
    profit = 0
    state={'day':0, 'num_stock':num_stock,'profit':profit}

    # first day we buy
    actions = generateNextActions('b', state= state)
    for action in actions:
       applyAction(state, 0, prices[0], action)


    # first day we cooldown
    actions = generateNextActions('c', state= state)
    for action in actions:
       applyAction(state, 0, prices[0], action)